import networkx as nx
import numpy as np

from branch_device import Resistor, IndependentCurrentSource


class NodalAnalysis:

    def __init__(self, graph):
        """
        Constructor
        :param graph: Graph of the network to analyze
        """
        self.graph = graph

    def solve(self, reference_node):
        """
        TODO Only handles the case of Resistors + independent current sources, should also handle VCT
        :param reference_node: reference node used for the solution
        :return: a map: node -> node potential
        """

        # 1. Build G_N
        passified_graph = nx.MultiDiGraph()  # Directed graph with multi-edges
        for (u, v, d) in self.graph.edges(data=True):
            if isinstance(d['device'], Resistor):
                passified_graph.add_edge(u, v, device=d['device'])

        n_edges = passified_graph.number_of_edges()  # Number of edges of the passified graph
        n_nodes = passified_graph.number_of_nodes()  # Number of nodes of the graph

        nodeId = dict(zip(passified_graph.nodes(), range(n_nodes)))  # Create a map: node -> integer id, for indexing
        edgeId = dict(zip(passified_graph.edges(), range(n_edges)))  # Create a map: edge -> integer id, for indexing

        A = np.zeros((n_nodes, n_edges))  # Create A matrix filled with zeros
        G_B = np.zeros((n_edges, n_edges))  # Create G_B matrix filled with zeros
        for (u, v, d) in passified_graph.edges(data=True):
            A[nodeId[u], edgeId[u, v]] = 1  # Edge starts from u
            A[nodeId[v], edgeId[u, v]] = -1  # Edge points to v
            G_B[edgeId[u, v], edgeId[u, v]] = d['device'].conductance  # Branch conductance on the diagonal

        A = np.delete(A, nodeId[reference_node], 0)  # Remove row of reference node

        G_N = A.dot(G_B).dot(A.transpose())  # Compute G_N from A and G_B

        # 2. Build i_sN
        i_sN = np.zeros((n_nodes, 1))
        for (u, v, d) in self.graph.edges(data=True):
            if isinstance(d['device'], IndependentCurrentSource):
                i_sN[nodeId[u]] -= d['device'].current  # Edge starts from u
                i_sN[nodeId[v]] += d['device'].current  # Edge points to v

        i_sN = np.delete(i_sN, nodeId[reference_node], 0)  # Remove row of reference node

        # 3. Compute v_N
        v_SN = np.linalg.solve(G_N, i_sN)

        nodes = set(passified_graph.nodes()).difference(reference_node)
        return dict(zip(nodes, v_SN))

    def print_graph(self):
        print("Graph: ")
        for (u, v, d) in self.graph.edges(data=True):
            print("\t %s -> %s: %s" % (u, v, d["device"]))
        print("")


if __name__ == "__main__":
    # Create the graph of the network
    graph = nx.MultiDiGraph()  # Create and empty graph object. This is a directed graph with multi-edges.
    # Caution: sense matters!
    graph.add_edge("e", "a", device=Resistor("R1", 1.0 / 2.0))  # Add a resistor between nodes "e" and "a"
    graph.add_edge("e", "b", device=Resistor("R2", 1.0 / 5.0))
    graph.add_edge("e", "b", device=IndependentCurrentSource("I1", 2.5))  # Add an ICS between nodes "e" and "b"
    graph.add_edge("e", "c", device=Resistor("R3", 1.0 / 4.0))
    graph.add_edge("e", "c", device=IndependentCurrentSource("I2", 1.0))
    graph.add_edge("e", "d", device=IndependentCurrentSource("I3", 1.0))
    graph.add_edge("e", "d", device=Resistor("R3", 1.0 / 5.0))
    graph.add_edge("a", "b", device=Resistor("R4", 1.0 / 3.0))
    graph.add_edge("b", "c", device=Resistor("R5", 1.0 / 2.0))
    graph.add_edge("c", "d", device=Resistor("R6", 1.0 / 10.0))
    graph.add_edge("a", "c", device=Resistor("R7", 1.0 / 3.0))
    graph.add_edge("a", "c", device=IndependentCurrentSource("I4", 3.0))
    graph.add_edge("b", "d", device=Resistor("R8", 1.0 / 7.0))

    # Instantiate the solver and display the graph
    N = NodalAnalysis(graph)
    N.print_graph()

    # Solve and print the solution
    solution = N.solve(reference_node="e")
    print("Node potentials:")
    print("\n".join("\t %s: %.4f" % (k, v) for (k, v) in solution.items()))
    print("")
