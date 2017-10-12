# create a class point which is a representation of 2D point.

# write a class rectangle with attributes: width, height and method area
class Rectangle(object):
    def __init__(self, sides):
        self.width= sides[0]
        self.height= sides[1]
    def area(self):
        self.rect_area= self.width * self.height
        return self.rect_area

rect= Rectangle((3,4))

print(f"The width is {rect.width}, the height is {rect.height}, for this rectangle the area is {rect.area()}")