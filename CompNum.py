import math

# Checks to ensure that arguments passed are complex numbers or of valid type to convert to complex number format
def arg_check(arg):
    if type(arg) != CompNum:
        if type(arg) == int or type(arg) == float:
            return CompNum(arg)
        else:
            raise ValueError("All arguments must be of a numeric type.")
    else:
        return arg

class CompNum:
    def __init__(self, real=0, imag=0, polar=False):
        # Verify that all arguments are of numeric type
        if (type(real) == int or type(real) == float) and (type(imag) == int or type(imag) == float):
            # Convert input arguments from polar to cartesian
            if polar:
                self.real = real * math.sin(imag)
                self.imag = real * math.cos(imag)
            else:
                self.real = float(real)
                self.imag = float(imag)
        else:
            raise ValueError("All arguments must be of a numeric type.")

    # Return string showing complex number in "a + bi" format
    def __str__(self):
        if self.imag < 0:
            operation = '-'
        else:
            operation = '+'
        return "{0} {1} {2}i".format(round(self.real, 2), operation, round(abs(self.imag), 2))

    def __add__(self, arg):
        arg = arg_check(arg)
        return CompNum(self.real + arg.real, self.imag + arg.imag)

    def __sub__(self, arg):
        arg = arg_check(arg)
        return CompNum(self.real - arg.real, self.imag - arg.imag)

    def __mul__(self, arg):
        arg = arg_check(arg)
        # Determine product by good old FOIL
        return CompNum(self.real * arg.real - self.imag * arg.imag, self.real * arg.imag + self.imag * arg.real)

    def __truediv__(self, arg):
        arg = arg_check(arg)
        # Determine the conjugate of the divisor
        conjugate = CompNum(arg.real, -1 * arg.imag)
        # Calculate numerator and denominator multiplied by conjugate
        num = self * conjugate
        den = (arg * conjugate).real
        if den == 0:
            raise ZeroDivisionError
        else:
        # Calculate quotient
            return CompNum(num.real / den, num.imag / den)

    def __pow__(self, arg):
        arg = arg_check(arg)

    def __eq__(self, arg):
        arg = arg_check(arg)
        if self.real == arg.real and self.imag == arg.imag:
            return True
        else:
            return False

    def __ne__(self, arg):
        return not (self == arg)

    # Calculate radial polar coordinate
    def magnitude(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    # Calculate angular polar coordinate in radians
    def dir_radian(self):
        if self.imag == 0:
            if self.real > 0:
                return math.pi / 2
            elif self.real < 0:
                return math.pi / -2
            else:
                return 0
        else:
            return math.atan(self.real / self.imag)

    # Calculate angular polar coordinate in degrees
    def dir_degrees(self):
        return math.degrees(self.dir_radian())
