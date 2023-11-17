from abc import ABC, abstractmethod

# pierwszy przykład - klasy abstrakcyjne
class Shape (ABC):

    @abstractmethod
    def area(self):
        pass

class Square (Shape):

    def __init__(self, side):
        self.side = side

    def area (self):
        return self.side * self.side
    
class Rectangle (Shape):

    def __init__(self, firstSide, secondSide):
        self.firstSide = firstSide
        self.secondSide = secondSide
    
    def area (self):
        return self.firstSide * self.secondSide
    
square = Square(10)
restangle = Rectangle(10, 2)

print (square.area())
print (restangle.area())
print('---')

# drugi przykład - klasy abstrakcyjne
class Figure (ABC):

    @abstractmethod
    def area(self):
        pass

class SquareTwo (Figure):
    def __init__(self, length):
        self.length = length

    def areaTwo(self):
        return self.length * self.length
    
try:
    Figure()
except TypeError as error:
    print(error)


print('---')
# trzeci przykład - klasy abstrakcyjne
class Param (ABC):

    @abstractmethod
    def perimeter():
        pass

    @abstractmethod
    def area():
        pass

class SquareThree (Param):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side
    
    def area(self):
        return self.side * self.side
    
testSquare = SquareThree(10)

print(testSquare.perimeter())
print(testSquare.area())
print('---')

# czwarty przykład
class TaxPayer(ABC):
    @abstractmethod 
    def calculate_tax():
        pass

class Salary (TaxPayer):
    def __init__(self, salary):
        self.salary = salary
    
class StudentTaxPayer (TaxPayer):
    def __init__(self, money):
        self.money = money

    def calculate_tax(self):
        return 0.15 * self.money
    
class DisabledTaxPayer (TaxPayer):
    def __init__(self, salary):
        self.salary = salary

    def calculate_tax(self):
        return min(0.12 * self.salary, 5000.0)
    
student = StudentTaxPayer(40000)
disabled = DisabledTaxPayer(50000)

print(student.calculate_tax())
print(disabled.calculate_tax())

# 