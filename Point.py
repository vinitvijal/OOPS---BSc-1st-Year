# WAP to define a class Point with coordinates x and y as attributes.
# Create relevant methods and print the objects. Also define 
# a method distance to calculate the distance between any two point objects.

class Point:
    x = 0 
    y = 0 

    def __init__(self, x, y):
        self.x = x
        self.y = y   

    def distance(self, other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2 )**0.5

    def __str__(self):
        return str((self.x, self.y))


# l = list((1,2,3))
# print(l)

p1 = Point(2,-7)
p2 = Point(4,5)

print(p1.distance(p2))