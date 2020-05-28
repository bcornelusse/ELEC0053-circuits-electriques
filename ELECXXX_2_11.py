from RSE.impedance import Impedance
from RSE.phasor import Phasor
import math

# Power factor compensation

frequency = 50

# Data
Va: Phasor = Phasor(math.sqrt(2)*100, math.pi/6)


Vb: Phasor = Va.shift(2*math.pi/3)
Vc: Phasor = Va.shift(-2*math.pi/3)
Vab: Phasor = Va - Vb

print(Va.time_domain_expression(frequency))
print(Vb.time_domain_expression(frequency))
print(Vc.time_domain_expression(frequency))
print(Vab.time_domain_expression(frequency))
