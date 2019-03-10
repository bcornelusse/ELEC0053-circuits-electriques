# Exercise 2.3
from RSE.impedance import Impedance

omega = 1000  # rad /s
Z_R = Impedance(5e3, 0)
Z_C = Impedance(0, -1 / (omega * 49.8e-6))
Z_L = Impedance(0, omega * 20e-3)

Z = Z_R + Z_C.parallel(Z_L)

Z.tex_cart()
Z.tex_polar()

Z_1 = Impedance(2e3, omega * 10e-3)

Z_eq = Z_1 + Z

Z_eq.tex_cart()
Z_eq.tex_polar()

E = complex(100, 0)

# Compute currents.
I_1 = E/Z_eq.Z
I_R2 = E / Impedance(4e3, 0).Z
I = I_1 + I_R2

# Compute voltages.
U_R2 = E
U_R1 = Impedance(2e3,0).Z * I_1
U_L1 = Impedance(0,omega*10e-3).Z * I_1
U_Z1 = Z_1.Z * I_1
U_Z = Z.Z * I_1

# Plot voltages.
from matplotlib import pyplot as plt
f, (ax1, ax2) = plt.subplots(1, 2)
for U in [E, U_Z1, U_Z]:
    ax1.plot([0, U.real], [0, U.imag], marker='o')
ax1.set_xlim((0, 110))
ax1.set_ylim((-50, 50))
ax1.set_ylabel('Imaginary')
ax1.set_xlabel('Real')

# Plot currents.
for i in [I, I_1, I_R2]:
    ax2.plot([0, i.real], [0, i.imag], marker='o')
ax2.set_xlim((0, 0.04))
ax2.set_ylim((-0.02, 0.02))
ax2.set_ylabel('Imaginary')
ax2.set_xlabel('Real')

plt.show()
