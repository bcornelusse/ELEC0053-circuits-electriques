import networkx as nx
from numpy.testing import assert_allclose

from general_methods.branch_device import Resistor, IndependentCurrentSource
from general_methods.nodal_analysis import NodalAnalysis

_EPS = 1e-4


def ex_1_20_test():
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

    assert (solution["a"] - (-0.112004) < _EPS)
    assert (solution["b"] - (0.306512) < _EPS)
    assert (solution["c"] - (0.394812) < _EPS)
    assert (solution["d"] - (0.322441) < _EPS)
    assert (solution["e"] - (0.000000) < _EPS)
