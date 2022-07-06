"""
Method overriding is an ability of any object-oriented programming language
that allows a subclass or child class to provide a specific implementation of
a method that is already provided by one of its super-classes or parent classes.
When a method in a subclass has the same name, same parameters or signature and
same return type(or sub-type) as a method in its super-class, then the method
in the subclass is said to override the method in the super-class.
"""
# Defining parent class
class Parent:
    # Constructor
    def __init__(self):
        self.value = "This is Parent"

    # Parent's show method
    def show(self):
        print(self.value)


# Defining child class
class Child(Parent):
    # Constructor
    def __init__(self):
        self.value = "This is  Child"

    # Child's show method
    def show(self):
        print(self.value)


# Driver's code
parent_obj = Parent()
child_obj = Child()

# parent_obj.show()
# child_obj.show()

# Output:
# Inside Parent
# Inside Child
# =========================Using Super()=========================================
"""
Using Super(): Python super() function provides us the facility to refer
to the parent class explicitly. It is basically useful where we have to call
superclass functions. It returns the proxy object that allows us to refer parent class by super.

 """
# Program to define the use of super()
# function in multiple inheritance
class GFG1:
    def __init__(self):
        print("HEY !!!!!! GfG I am initialised(Class GEG1)")

    def sub_GFG(self, b):
        print("Printing from class GFG1:", b)


# class GFG2 inherits the GFG1
class GFG2(GFG1):
    def __init__(self):
        print("HEY !!!!!! GfG I am initialised(Class GEG2)")
        super().__init__()

    def sub_GFG(self, b):
        print("Printing from class GFG2:", b)
        super().sub_GFG(b + 1)


# class GFG3 inherits the GFG1 ang GFG2 both
class GFG3(GFG2):
    def __init__(self):
        print("HEY !!!!!! GfG I am initialised(Class GEG3)")
        super().__init__()

    def sub_GFG(self, b):
        print("Printing from class GFG3:", b)
        super().sub_GFG(b + 1)

"""
main function When you start working with other people's code you will run into
the if __name__ == '__main__' function at the end of the Python code.
 this function checkS whether you run  the module (or script) "directly",
or if you import the module from another one
"""
if __name__ == "__main__":

    # created the object gfg
    gfg = GFG3()

    # calling the function sub_GFG3() from class GHG3
    # which inherits both GFG1 and GFG2 classes
    gfg.sub_GFG(10)

# OutPut:
    # HEY !!!!!! GfG I am initialised(Class GEG3)
    # HEY !!!!!! GfG I am initialised(Class GEG2)
    # HEY !!!!!! GfG I am initialised(Class GEG1)
    # Printing from class GFG3: 10
    # Printing from class GFG2: 11
    # Printing from class GFG1: 12
# ========Method overriding with multiple and multilevel inheritance==============
# Python program to demonstrate
# overriding in multiple inheritance


# Defining parent class 1
class Parent1:

    # Parent's show method
    def show(self):
        print("Inside Parent1")


# Defining Parent class 2
class Parent2:

    # Parent's show method
    def display(self):
        print("Inside Parent2")


# Defining child class
class Child(Parent1, Parent2):

    # Child's show method
    def show(self):
        print("Inside Child")


# Driver's code
# obj = Child()

# obj.show()
# obj.display()

# Output:Inside Child
# Inside Parent2
