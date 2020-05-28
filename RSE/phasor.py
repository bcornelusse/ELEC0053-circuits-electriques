import math
import cmath
import numpy as np
from RSE.impedance import Impedance


class Phasor:
    def __init__(self, mag, ang, type=None):
        """
        Phasor constructor.

        :param value: rms valur of the magnitude [depends on type].
        :param angle: phase shift [rad].
        :param type: type of phasor, either "current" or "voltage"
        """
        self.mag = mag
        self.ang = ang
        self.type = type
        # representation as a complex number.
        self._A = cmath.rect(mag, ang)

    @property
    def ang(self):
        return self._ang

    @ang.setter
    def ang(self, value):
        self._ang = value
        try:
            self._A = cmath.rect(self.mag, self.ang)
        except AttributeError:
            pass

    @property
    def mag(self):
        return self._mag

    @mag.setter
    def mag(self, value):
        self._mag = value
        try:
            self._A = cmath.rect(self.mag, self.ang)
        except AttributeError:
            pass

    def time_domain_expression(self, frequency):
        return "%.2f cos(%.2f t + %.2f [deg])" % (self.mag*np.sqrt(2), 2*math.pi*frequency, self.ang)

    def __add__(self, other):
        """
        Override addition.

        :param other: Another phasor.
        :return: The sum of this and the other impedance.
        """
        tmp = self._A + other._A
        return Phasor(*cmath.polar(tmp))

    def __sub__(self, other):
        """
        Override addition.

        :param other: Another phasor.
        :return: The sum of this and the other impedance.
        """
        tmp = self._A - other._A
        return Phasor(*cmath.polar(tmp))

    def __truediv__(self, other):
        """
        Override (true) division

        :param other: Another object that is represented as a complex number.
        :return: The quotient of this and the other impedance or phasor.
        """
        # Could divide the Z simply, but to show the details.
        mag = self.mag / other.mag
        ang = self.ang - other.ang
        return Phasor(mag, ang)

    def times(self, other: Impedance):
        """
        Override multiplication

        :param other: Another impedance.
        :return: The product of this and the other impedance.
        """
        # Could multiply the Z simply, but to show the details.
        mag = self.mag * other.mag
        ang = self.ang + other.ang
        return Phasor(mag, ang)

    def herm(self, other):
        "Hermitian product"
        return self._A * other._A.conjugate()

    def shift(self, angle, inplace=False):
        """
        :param angle: shift angle [rad].
        """
        if inplace:
            self.ang += angle
        else:
            ang = self.ang + angle
            return Phasor(self.mag, ang)

    def __str__(self):
        return '%.2f < %.2f [deg]' % (self.mag, self.ang*180/math.pi)
