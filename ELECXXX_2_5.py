from RSE.impedance import Impedance
from RSE.phasor import Phasor
import math

# Input data
V = Phasor(100, 0)
Z_L = Impedance(0, 0.1)
Z_R = Impedance(2, 0)
Z_C = Impedance(0, -5)

# Equivalent impedance
Z_eq = Z_L + Z_R.parallel(Z_C)
print("Equivalent impedance: ", Z_eq)

# Current
I = V/Z_eq
print("Current: ", I)

# Complex power consumed
S = V.herm(I)
# Reactive power consumed
print("Q = %.2f var" % S.imag)

# Recompute the complex power from the power consumed by L (>0) and the power consumed by C (<0)
Q_L = Z_L.X * I.mag**2
I_C = I.times(Z_R/(Z_R+Z_C))
Q_C = Z_C.X * I_C.mag**2

print("Q_L+Q_C = %.2f var" % (Q_L+Q_C))
print("Q_L = %.2f var" % (Q_L))
print("Q_C = %.2f var" % (Q_C))
