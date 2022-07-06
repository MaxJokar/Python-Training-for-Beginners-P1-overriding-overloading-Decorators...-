"""
Experience about Decorators in Python
"""
def my_wrapper(my_func2):
    """
    we are experiencing How to use a decorator
             in Python .
    """

    def my_innder_func():
        print("Inside wrapper")
        my_func2()  # Helps to print Hello Decorator
    return my_innder_func()


@my_wrapper
def my_func():
    """This function is called with its decorator passed to my_wrapper
    """
    print("Hello Decorator")


my_func()  # python -m flake8 ./decoratortest.py  DONE  python -m black ./decoratortest.py

# =====================================================================================
# def mydecorator(fn):
#     """The mydecorator() function  takes a function OR
#     (any function that does not take any argument) as an argument. The inner function
#     inner_function() can access the outer function's argument, so it executes some code
#     before or after to extend the functionality before calling the argument function.
#     The mydecorator function returns an inner function.


#     """

#     def inner_function():
#         greet()
#         print("How are you?")

#     return inner_function


# @mydecorator
# def greet():
#     print("Hello! ", end=" ")


# greet()  # python -m black ./decoratortest.py

# Output:Hello! How are you?

# =========================================================
# def mydecorator(fn):
#     def inner_function():
#         fn()
#         print("How are you?")

#     return inner_function


# @mydecorator
# def dosomething():
#     print("I am doing something.", end="")


# dosomething()

# outPut: I am doing something.How are you?
