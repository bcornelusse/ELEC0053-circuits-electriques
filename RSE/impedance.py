import numpy as np


class Impedance:
    def __init__(self, R, X):
        """
        Impedance constructor.

        :param R: Resistance [Ohm].
        :param X: Reactance [Ohm].
        """
        self.R = R
        self.X = X
        self.Z = complex(R, X)  # representation as a complex number.
        self.mag = np.abs(self.Z)  # Magnitude.
        self.ang = np.angle(self.Z)  # Angle in rad.

    @staticmethod
    def from_polar(mag, ang):
        """
        Use this if you want to build an impedance from its magnitude - angle description.
        :param mag: Magnitude [Ohm].
        :param ang: Angle [rad].
        :return: An Impedance object.
        """
        return Impedance(mag * np.cos(ang), mag * np.sin(ang))

    def __add__(self, other):
        """
        Override addition.

        :param other: Another impedance.
        :return: The sum of this and the other impedance.
        """
        return Impedance(self.R + other.R, self.X + other.X)

    def __mul__(self, other):
        """
        Override multiplication

        :param other: Another impedance.
        :return: The product of this and the other impedance.
        """
        # Could multiply the Z simply, but to show the details.
        mag = self.mag * other.mag
        ang = self.ang + other.ang
        return self.from_polar(mag, ang)

    def __truediv__(self, other):
        """
        Override (true) division

        :param other: Another impedance.
        :return: The quotient of this and the other impedance.
        """
        # Could devide the Z simply, but to show the details.
        mag = self.mag / other.mag
        ang = self.ang - other.ang
        return self.from_polar(mag, ang)

    def parallel(self, other):
        """
        Compute the equivalent impedance of this impedance in parallel with another.

        :param other: Another impedance.
        :return: The equivalent impedance.
        """
        num = self * other
        den = self + other
        return num / den

    def tex_cart(self):
        """
        Print impedance in latex format, R+jX style.
        """
        print("$ %.2f+j%.2f $" % (self.R, self.X))

    def tex_polar(self):
        """
        Print impedance in latex format, polar style.
        """
        print("$ %.2f \\angle %.2f $" % (self.mag, np.rad2deg(self.ang)))


if __name__ == "__main__":

    # Exercise 2.3
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
