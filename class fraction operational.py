class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        try:
            self.numerator = int(numerator)
            self.denominator = int(denominator)
        except ValueError:
            raise TypeError(" numerator and denominator could not be converted to integers")
        if not (isinstance(numerator, int) and isinstance(denominator, int)):
            raise TypeError(" numerator and denominator must be integers")

        if numerator == 0:
            self.numerator = 0
            self.denominator = 1
        else:
            if (numerator < 0 and denominator >= 0 or numerator >= 0 and denominator < 0):
                sign = -1
            else :
                sign = 1
            a = abs(numerator)
            b = abs(denominator)
            while a% b != 0:
                tempA = a
                tempB = b
                a = tempB
                b = tempA % tempB
            self.numerator = abs(numerator) / b * sign
            self.denominator = abs(denominator) / b


    def __str__(self):
        if self.denominator == 0:
            return "Denominator cannot be zero"  
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if not isinstance(other, (Fraction, int)):
            raise TypeError("Can only add Fraction objects or integers")

        if isinstance(other, int):
            other = Fraction(other, 1)  
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if not isinstance(other, (Fraction, int)):
            raise TypeError("Can only subtract Fraction objects or integers")

        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self, other):
        if not isinstance(other, (Fraction, int)):
            raise TypeError("Can only multiply Fraction objects or integers")

        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __truediv__(self, other):
        if not isinstance(other, (Fraction, int)):
            raise TypeError("Can only multiply Fraction objects or integers")

        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)
    
    def __floordiv__(self, other):
        if not isinstance(other, (Fraction, int)):
            raise TypeError("Can only perform floor division with Fraction objects or integers")

        if isinstance(other, int):
            other = Fraction(other, 1)
        result = self.numerator // (other.numerator * self.denominator)
        return Fraction(result, self.denominator)



