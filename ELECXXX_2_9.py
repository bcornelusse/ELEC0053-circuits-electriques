from RSE.impedance import Impedance
from RSE.phasor import Phasor
import math

# Power factor compensation


# Data
V = Phasor(120, 0)
f = 60
omega = 2*math.pi*f
P_L = 1858.4
Q_L = 1031.3
S_L = complex(P_L, Q_L)
desired_pf = 0.9  # And leading

# Current power factor
pf = P_L/abs(S_L)
print(pf)  # Lagging since Q_L > 0

# Needed Q for desired power factor
new_Q = -math.sqrt(P_L**2 / desired_pf**2 - P_L**2)
print(new_Q)  # Leading since < 0

# Check
new_S = complex(P_L, new_Q)
new_pf = P_L/abs(new_S)
print(new_pf)

# Which C do we need to add ? It must consume Q_C
Q_C = -(Q_L - new_Q)
# As it is in parallel to the load, it is subject to the same voltage:
X_C = V.mag**2 / Q_C
print("Reactance: %.2e [Ohm]" % X_C)
# Thus
C = -1/(omega*X_C)
print("Capacity: %.2e [F]" % C)

# Final check
Z_C = Impedance(0, X_C)
Z_init = Impedance(0.3, 0.5) + Impedance(7, 0.2).parallel(Impedance(0, 15))
Z_eq = Z_C.parallel(Z_init)
S = V.mag**2/Z_eq.Z
print("Power factor = %.2e" % (S.real/abs(S)))
