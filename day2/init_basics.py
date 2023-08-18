class Circle:
    def __init__(self,pi):
        self.pi = pi

    def calc_area(self,r):
        return self.pi*r**2

carea = Circle(3.14)

print("Area of circle ",carea.calc_area(5))