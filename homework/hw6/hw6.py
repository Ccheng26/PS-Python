import math
class Shapes(object):
    def __init__(self,sides):
        self.sides= sides
        if sides==4:
            shape_type=input("Rectangle or Square ")
            if shape_type== "rectangle":
                side_len=input("Enter the length and width separated by a space: ")
                lens= side_len.split(" ")
                self.shape_is="rectangle"
                self.length=int(lens[0])
                self.width=int(lens[1])
            elif shape_type== "square":
                self.shape_is="square"
                side_len=input("Enter the length: ")
                self.length= int(side_len)
        elif sides==3:
            self.shape_is="triangle"
            side_len=input("Enter the lengths of the triangle separated by a space: ")
            lens= side_len.split(" ")
            self.a=int(lens[0])
            self.b=int(lens[1])
            self.c=int(lens[2])
        elif sides ==8:
            self.shape_is="octagon"
            side_len=input("An octagon has 8 equal sides. Enter the length of the side: ")
            self.length= int(side_len)
    def area(self):
        if self.sides==4 and self.shape_is=="square":
            return math.pow(self.length,2)
        elif self.sides==4 and self.shape_is=="rectangle":
            return self.length*self.width
        elif self.sides==3:
            # using heron's formula
            # (p((p-a)*(p-b)*(p-c)))^1/2, where p is equal to 1/2 the perimeter
            p = (self.a+self.b+self.c)/2
            area = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
            if area == 0.0 or 0:
                self.shape_is="not triangle"
                return "That's not a triangle"
            else:
                return area
        elif self.sides==8:
            return 2*(1+math.sqrt(2))*math.pow(self.length,2)
    def perimeter(self):
        # iterate over the amount of sides and add
        if self.sides==4 and self.shape_is=="square":
            return self.length*4
        elif self.sides==4 and self.shape_is=="rectangle":
            return 2*(self.length+self.width)
        elif self.sides==3 and self.shape_is=="triangle":
            return self.a+self.b+self.c
        elif self.sides==8:
            return 8*self.length


rectangle = Shapes(4)
print(f"Your {rectangle.shape_is} has a perimeter of {rectangle.perimeter()} and area of {rectangle.area()}")
square = Shapes(4)
print(f"Your {square.shape_is} has a perimeter of {square.perimeter()} and area of {square.area()}")
triangle = Shapes(3)
print(f"Your {triangle.shape_is} has a perimeter of {triangle.perimeter()} and area of {triangle.area()}")
octagon = Shapes(8)
print(f"Your {octagon.shape_is} has a perimeter of {octagon.perimeter()} and area of {octagon.area()}")