class Equilateral:
    a = 0

    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return 3 * self.a
    
    def area(self):
        return ((3**0.5) / 4) * (self.a**2)
    
    def height(self):
        return 2*self.area() / self.a
    

t = Equilateral(5)

print("Perimeter : ", t.perimeter())
print("Area : ", t.area())
print("Height : ", t.height())

print(t)