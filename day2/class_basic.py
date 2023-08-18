class Rectangle:
    def calc_area(self,length,breadth):
        print("Lenght ",length)
        print("Breadth ",breadth)
        return length*breadth

sur = Rectangle()
print("Area of rectangle is ",sur.calc_area(4,12))
