# def myWrapper(func):
#     """_summary_

#     Args:
#         func (_type_): _description_
#     """
#     def myInnderFunc():
#         print("Inside wrapper")
#         func() #Helps to print Hello Decorator
#     return myInnderFunc() 


# @myWrapper
# def myFunc():
#  print("Hello Decorator")


# myFunc()  NoneType' object is not callable
# myFunc
#=====================================================================================
# def mydecorator(fn):
#     """The mydecorator() function is the decorator function that takes a function 
#     (any function that does not take any argument) as an argument. The inner function
#     inner_function() can access the outer function's argument, so it executes some code 
#     before or after to extend the functionality before calling the argument function. 
#     The mydecorator function returns an inner function.


#     """
#     def inner_function():        
#         fn()
#         print('How are you?')
#     return inner_function


# @mydecorator
# def greet():
# 	print('Hello! ', end='')



# greet()

# Output:Hello! How are you?

#=========================================================
# def mydecorator(fn):

#     def inner_function():        
#         fn()
#         print('How are you?')
#     return inner_function


# @mydecorator
# def dosomething():
# 	print('I am doing something.', end='')


# dosomething()

#outPut: I am doing something.How are you?




