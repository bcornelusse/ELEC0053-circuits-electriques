import numpy as np

# Version 2019-2020

# Part 1: Todo

# Part 2
# We can write U = E_Th + R_Th * I with U and I the voltage and currents at ports 1 and 2, respectively
# We also know that U_1 = E, and that U_2 = -R_L * I_2, we know the values of E and R_L
# From that we can derive a system of equations for I
v = np.array([[20-21.65], [0-13.01]])
R = np.array([[26.52, 5.13], [5.13, 30+27.88]])
I = np.linalg.solve(R, v)  # I = v/R

# P(E)
P_E = 20 * I[0]  # I[0] = I_1
# P(R_L)
P_R_L = 30 * I[1] ** 2  # I[0] = I_2

print(P_E, P_R_L)
