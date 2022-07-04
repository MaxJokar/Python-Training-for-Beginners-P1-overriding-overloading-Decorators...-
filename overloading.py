
# First product method.
# Takes two argument and print their
# product

# def product(a, b):
#     """in Python :The problem with method overloading  is that
#     we may overload the methods but can only use the "latest defined method". 
#     """
#     p = a * b
#     print(p)
      
# Second product method
# Takes three argument and print their
# product
# def product(a, b, c):
#     p = a * b*c
#     print(p)
  
# Uncommenting the below line shows an error    
# product(4, 5)
  
# This line will call the second product method
# product(4, 5, 5)
#Output:100

#Error:missing 1 required positional argument: 'c'
# product(4, 5)

#========Method overriding with multiple and multilevel inheritance==============
# Python program to demonstrate
# overriding in multiple inheritance
  
  
# Defining parent class 1
class Parent1():
          
    # Parent's show method
    def show(self):
        print("Inside Parent1")
          
# Defining Parent class 2
class Parent2():
          
    # Parent's show method
    def display(self):
        print("Inside Parent2")
          
          
# Defining child class
class Child(Parent1, Parent2):
          
    # Child's show method
    def show(self):
        print("Inside Child")
     
        
# Driver's code
obj = Child()
  
obj.show()
obj.display()

# Output:Inside Child
# Inside Parent2
#=================================================================================




















