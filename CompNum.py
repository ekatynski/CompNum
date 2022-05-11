class CompNum:
    def __init__(self, real=0, imag=0):
        # Verify that all arguments are of numeric type
        if (type(real) == int or type(real) == float) and (type(imag) == int or type(imag) == float):
            self.real = float(real)
            self.imag = float(imag)
        else:
            raise ValueError("All arguments must be of a numeric type.")

    def __str__(self):
        if self.imag < 0:
            operation = '-'
        else:
            operation = '+'
        return "{0} {1} {2}i".format(round(self.real, 2), operation, round(abs(self.imag), 2))

    def __add__(self, arg):
        if type(arg) != CompNum:
            arg = CompNum(arg)
        return CompNum(self.real + arg.real, self.imag + arg.imag)
        

    def __sub__(self, arg):
        if type(arg) != CompNum:
            arg = CompNum(arg)
        return CompNum(self.real - arg.real, self.imag - arg.imag)

    def __mul__():
        pass

    def __truediv():
        pass


        