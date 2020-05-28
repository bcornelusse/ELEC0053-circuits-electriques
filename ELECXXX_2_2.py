from RSE.impedance import Impedance
from RSE.phasor import Phasor
import math

V = Phasor(120, 0)

f = 60
omega = 2 * math.pi * f

R = 1.5
L = 2e-3
C = 100e-6
Z = Impedance(R, omega*L-1/(omega*C))

I = V / Z

print("I = %s" % I)
print("i(t) = " + I.time_domain_expression(f))
