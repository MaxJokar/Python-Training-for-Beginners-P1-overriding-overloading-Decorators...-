# Python program to demonstrate
# method overriding


# Defining parent class
class Parent:
    """Method overriding is an ability of any object-oriented programming language
    that allows a subclass or child class to provide a specific implementation of
    a method that is already provided by one of its super-classes or parent classes.
    When a method in a subclass has the same name, same parameters or signature and
    same return type(or sub-type) as a method in its super-class, then the method
    in the subclass is said to override the method in the super-class.
    """
#python -m black ./overriding.py 

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

#Output:
#Inside Parent
# Inside Child
#=========================Using Super()=========================================
# Program to define the use of super() 
# function in multiple inheritance 
class GFG1: 
    """Using Super(): Python super() function provides us the facility to refer 
    to the parent class explicitly. It is basically useful where we have to call
    superclass functions. It returns the proxy object that allows us to refer parent class by ‘super’.
    """
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG1)') 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG1:', b) 
    
# class GFG2 inherits the GFG1 
class GFG2(GFG1): 
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG2)') 
        super().__init__() 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG2:', b) 
        super().sub_GFG(b + 1) 
    
# class GFG3 inherits the GFG1 ang GFG2 both 
class GFG3(GFG2): 
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG3)') 
        super().__init__() 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG3:', b) 
        super().sub_GFG(b + 1) 
    
    
# main function 
#When you start working with other people's code you will run into
# the if __name__ == '__main__' function at the end of the Python code. 
#  this function checkS whether you run  the module (or script) directly, 
# or if you import the module from another one
if __name__ == '__main__': 
    
    # created the object gfg 
    gfg = GFG3() 
    
    # calling the function sub_GFG3() from class GHG3 
    # which inherits both GFG1 and GFG2 classes 
    gfg.sub_GFG(10)