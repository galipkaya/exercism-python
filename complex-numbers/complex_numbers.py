from math import sqrt
from math import exp
from math import sin
from math import cos

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real+other.real, self.imaginary+other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                      self.imaginary * other.real + self.real * other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real-other.real, self.imaginary-other.imaginary)

    def __truediv__(self, other):
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        return ComplexNumber((a * c + b * d)/(c**2 + d**2), (b * c - a * d)/(c**2 + d**2))

    def __abs__(self):
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        # (e^x)*(cos(y) + j*sin(y))
        # (e^x)*cos(y) + j*(e^x)*sin(y)
        return ComplexNumber(exp(self.real) * cos(self.imaginary),
                             (exp(self.real) * sin(self.imaginary)))
