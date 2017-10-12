# create a class point which is a representation of 2D point.
class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print(self):
        print(f"The x coordinate is {self.x} and the y coordinate is {self.y}")

point= Point(5,3)
point.print()

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

"""class Person:
    def __init__(self, in, lb):
        self.height = in
        self.weight = lb

    def height_is():
        if self.height == height:
            print(self.height, "is your height")

    def weight_is():
        if self.weight == weight:
            print(self.weight, "is your weight")

show = Person(120, 160)
show.height_is()
show.weight()"""

class Employee:
    def __init__(self, f, l):
        self.firstName = f
        self.lastName = l

    def name(self):
        print(f"the person is: {self.firstName} {self.lastName}")

class Department(Employee):
    def __init__(self,f, l, d):
        Employee.__init__(self, f, l)
        self.department = d
    def name(self):
        print(f"the person is: {self.firstName} {self.lastName} from {self.department}")


p = Employee("saroosh", "zaman")
p.name()
p2 = Employee("fname", "lname")
p3 = Department("j", "m", "hr")
p3.name()