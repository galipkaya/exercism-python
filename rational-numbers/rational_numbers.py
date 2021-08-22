from __future__ import division
from math import gcd

class Rational:
    def __init__(self, numer, denom):
        self.numer, self.denom = self.reduce(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer, denom = self.find_sign(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)
        return Rational(numer, denom)

    def __sub__(self, other):
        numer, denom = self.find_sign(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)
        return Rational(numer, denom)

    def __mul__(self, other):
        numer, denom = self.find_sign(self.numer * other.numer, self.denom * other.denom)
        return Rational(numer, denom)

    def __truediv__(self, other):
        numer, denom = self.find_sign(self.numer * other.denom, self.denom * other.numer)
        return Rational(numer, denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power > 0:
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return Rational(self.denom ** -power, self.numer ** -power)

    def __rpow__(self, base):
        return (base**self.numer)**(1/self.denom)

    def find_sign(self, numer, denom):
        if numer == 0:
            return 0, 1
        if numer < 0 and denom < 0:
            return -numer, -denom

        return self.reduce(numer, denom)

    def reduce(self, numer, denom):
        if numer > 0 and denom < 0:
            numer = -numer
            denom = -denom
        divisor = gcd(int(numer), int(denom))
        return int(numer/divisor), int(denom/divisor)
