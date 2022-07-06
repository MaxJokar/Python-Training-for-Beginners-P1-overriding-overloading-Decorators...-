"""
Experience about Decorators in Python
"""
def my_wrapper(my_func2): #  receives my_func as an parameter
    """
    we are experiencing How to use a decorator
             in Python .my_wrapper get the function my_func here:
    """

    def my_innder_func():
        # print("Greeting:") #  prints Greeting:
        # print("I'm The Inside wrapper:",end=" ")
        my_func2()  # my_func is executed
    return my_innder_func()


@my_wrapper
def my_func():
    """This function is called with its decorator passed to my_wrapper
    """
    # print("Hello Decorator, How's it going ?")


# my_func()  # python -m flake8 ./decoratortest.py  DONE  python -m black ./decoratortest.py

# =====================================================================================
def mydecorator(greet2):
    """The mydecorator() function  takes a function OR
    (any function that does not take any argument) as an argument. The inner function
    inner_function() can access the outer function's argument, so it executes some code
    before or after to extend the functionality before calling the argument function.
    The mydecorator function returns an inner function.
    """

    def inner_function():
        """
        In here we add a Decorator then call the outer scope
        """
        # print("Greeting:")
        # greet2()
        # print("How are you?")

    return inner_function


@mydecorator
def greet():
    """
     recalled function greet with a decorator
    """
    # print("Hello! ", end=" ")


# greet()  # python -m black ./decoratortest.py

# Output:Hello! How are you?

# =========================================================
def mydecorators(fn2):
    """
       this method gets the fn2 function
    """
    def inner_function():
        fn2()
        print("How are you?")

    return inner_function


@mydecorators
def dosomething():
    """
    This is  Our Docstring
    """
    print("I am doing something.", end="")


dosomething()

# outPut: I am doing something.How are you?
