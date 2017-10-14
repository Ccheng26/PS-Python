class Parent(object):
    def implicit(self):
        print("Parent implicit()")

class Child(object):
    pass

dad=Parent()
son= Child()
dad.implicit()
son.implicit()
