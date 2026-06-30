import math


class Operation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate(self):
        raise NotImplementedError

    def __str__(self):
        return str(self.calculate())
#^^^ Parent class
#Ru: Родительский класс


#>>> STANDARD OPERATIONS
#Ru: АРЕФМЕТИЧЕСКИЕ ОПЕРАЦИИ

class Sum(Operation):
    def calculate(self):
        return self.x + self.y
#^^^ Addition operation (x + y)
#Ru: Операция сложения

class Sub(Operation):
    def calculate(self):
        return self.x - self.y
#^^^ Subtraction operation (x - y)
#Ru: Операция вычитания

class Mult(Operation):
    def calculate(self):
        return self.x * self.y
#^^^ Multiplication operation (x * y)
#Ru: Операция умножения

class Div(Operation):
    def calculate(self):
        if self.y == 0:
            raise ZeroDivisionError("division by zero")
        return self.x / self.y
#^^^ Division operation (x / y), takes into account division by zero
#Ru: Операция деления

class Pow(Operation):
    def calculate(self):
        if self.x == 0 and self.y < 0:
            raise ZeroDivisionError("cannot raise 0 to a negative power")
        try:
            return self.x ** self.y
        except OverflowError:
            raise OverflowError("result is too large!")
#^^^ Exponentiation operation (x ** y), takes into account the raising of zero to a negative power and buffer overflow
#Ru: Операция возведения в степень, учитывает возведение в нулевую степень и переполнение буфера

class Root(Operation):
    def calculate(self):
        if self.y == 0:
            raise ZeroDivisionError("degree of the root cannot be zero")
        if self.x < 0 and self.y % 2 == 0:
            raise ValueError("even root of a negative number")
        if self.x < 0:
            return -math.exp(math.log(abs(self.x)) / self.y)
        return math.exp(math.log(self.x) / self.y)
#^^^ Root calculation operation (x ** (1 / y)), takes into account degree of the root and even root of a negative number
#Ru: Операция корня степени y из x, учитывает степень корня и четный корень из отрицательного числа


#>>> TRIGONOMETRIC OPERATIONS
#Ru: ТРИГОНОМЕТРИЧЕСКИЕ ОПЕРАЦИИ

class Sin(Operation):
    def calculate(self):
        return math.sin(self.x)
#^^^ Sine operation (sin x)
#Ru: Операция синуса (синус из x)

class Cos(Operation):
    def calculate(self):
        return math.cos(self.x)
#^^^ Cosine operation (cos x)
#Ru: Операция косинуса (косинус из x)

class Tan(Operation):
    def calculate(self):
        return math.tan(self.x)
#^^^ Tangent operation (tan x)
#Ru: Операция тангенс (тангенс из x)

class Cot(Operation):
    def calculate(self):
        try:
            return 1 / math.tan(self.x)
        except ZeroDivisionError:
            raise ZeroDivisionError("cotangent is undefined")
#^^^ Cotangent operations (cot x)
#Ru: Операция котангенса (котангенс из x)
