# Exercise 4.3

from matplotlib import pyplot as plt
from RSE.impedance import Impedance


def print_complex(n: complex):
    return '({c.real:.2f} + {c.imag:.2f}i)'.format(c=n)


Z_1 = Impedance(3, 5)
Z_2 = Impedance(5, -6)
Z_0 = Impedance(2, 3)

Z_12 = Z_1.parallel(Z_2)
Z_tot = Z_0 + Z_12

E = complex(100, 0)

# Compute currents.
I = E/Z_tot.Z
V_12 = Z_0.Z * I
V_23 = Z_12.Z * I
I_Z1 = V_12 / Z_1.Z
I_Z2 = I - I_Z1

print("V_12 = %s" % print_complex(V_12))
print("V_23 = %s" % print_complex(V_23))

print("I = %s" % print_complex(I))
print("I_Z1 = %s" % print_complex(I_Z1))
print("I_Z2 = %s" % print_complex(I_Z2))


# Plot voltages.
f, (ax1, ax2) = plt.subplots(1, 2)
for U in [E, V_12, V_23]:
    ax1.plot([0, U.real], [0, U.imag], marker='o')
#ax1.set_xlim((0, 110))
#ax1.set_ylim((-50, 50))
ax1.set_ylabel('Imaginary')
ax1.set_xlabel('Real')

# Plot currents.
for i in [I, I_Z1, I_Z2]:
    ax2.plot([0, i.real], [0, i.imag], marker='o')
#ax2.set_xlim((0, 0.04))
#ax2.set_ylim((-0.02, 0.02))
ax2.set_ylabel('Imaginary')
ax2.set_xlabel('Real')

plt.show()
