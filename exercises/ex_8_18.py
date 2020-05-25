import numpy as np

# Version 2019-2020

# I have simplified the left branches before starting
# Mesh analysis
Raa = 70 / 3
Rab = np.array([70, 60]) / 3
Rba = np.array([[70], [60]]) / 3
Rbb = np.array([[160, 120], [120, 150]]) / 3
Rbbinv = np.linalg.inv(Rbb)
R_tmp = np.matmul(Rab, Rbbinv)
Rth = (Raa - np.matmul(R_tmp, Rba))

# Nodal analysis
Gaa = 2 / 20
Gab = np.array([-1, -1]) / 20
Gba = np.array([[-1], [-1]]) / 20
Gbb = np.array([[9, -2], [-2, 5]]) / 20
Gbbinv = np.linalg.inv(Gbb)
Gtemp = np.matmul(Gab, Gbbinv)
Gno = (Gaa - np.matmul(Gtemp, Gba))
