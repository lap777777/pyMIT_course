# OBJECT ORIENTED PROGRAMMING

# definice tridy
class Coordinate(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (y_diff_sq + x_diff_sq)**0.5

    # metoda pro tisk
    def __str__(self):
        return f"<{self.x}, {self.y}>"


# creating an object
c = Coordinate(10, 20)
origin = Coordinate(0, 0)
print(c.x)
print(origin.y)
print()

# pouziti metody
zero = Coordinate(0,0)
print(c.distance(zero))
# alternativni zapis
print(Coordinate.distance(c, zero))
print()

#tisk
print(c)
print()


class Fraction(object):
    """
    A number represented as a fraction
    """

    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom
    
    def __str__(self):
        """Returns a string represenation of object"""
        return str(self.num) + '/' + str(self.denom)

    def __add__(self, other):
        """Returns a new fraction representing the addition"""
        top = self.num * other.denom + self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """Returns a new fraction representing the substraction"""
        top = self.num*other.denom - self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __float__(self):
        """returns a float value of the fraction"""
        return self.num/self.denom

    def inverse(self):
        """returns a new fraction representation with switched num and denom"""
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
print(a)
b = Fraction(3, 4)
print(b)
c = a + b   # __add__ method used
d = b - a   # __sub__ method used
print(c)
print(d)
print(float(c))
print(Fraction.__float__(c))
print(b.inverse())
print(float(b.inverse()))
print()

class Car(object):

    def __init__(self, w, d):
        self.wheels = w
        self.doors = d
        self.color = ""

    def paint(self, c):
        self.color = c

    def __str__(self):
        return f"Auto: kola: {self.wheels}, dvere: {self.doors}, barva: {self.color}"

    def __eq__(self, other):
        if self.wheels == other.wheels and self.doors == other.doors and self.color == other.color:
            return True
        else:
            return False


car1 = Car(4, 2)
car1.paint("white")
print(car1)
car2 = Car(6, 4)
Car.paint(car2, "black")
print(car2)
print(car1==car2)
print()
