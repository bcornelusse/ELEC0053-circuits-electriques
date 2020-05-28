from RSE.impedance import Impedance
from RSE.phasor import Phasor
import math

# Power factor compensation

# Data
Vr = Phasor(95, 0)  # [V]
Vs_mag = 100  # [V]
X = 1.5  # [Ohm]
P = 1000  # [W]

# Computation of Vs angle: P = (Vs*Vr*sin(delta))/X

delta = math.asin((P*X)/(Vs_mag*Vr.mag))
print("Angle difference: %.2e [deg]" % (delta*180/math.pi))
Vs = Phasor(Vs_mag, delta)

# The current flowing
I = (Vs-Vr) / Impedance(0, X)
print("Current: %s" % I)

# The complex power supplied
S = Vs.herm(I)
print("Reactive power supplied: %.2e [var]" % S.imag)
