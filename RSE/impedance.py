import numpy as np


class Impedance:
    """
    Used in ex_2_3.
    """
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
