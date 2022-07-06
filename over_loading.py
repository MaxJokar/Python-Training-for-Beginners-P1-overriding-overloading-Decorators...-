"""
We are  experiencing overLoading in Python . two functions with the same name and different
parameters amount give error . To solve this we have  a   technique!
"""


def product(a, b):
    """
    in Python :The problem with method overloading  is that
    we may overload the methods but can only use the "latest defined method".
    """
    p = a * b
    print(f"The amount of two parameters  is : {p}")
    print("The amount you found is ".format(p))

    """
    Second product method
    Takes three argument and print their
    product:but in Python the last function is prior to the previous one.
    """


def product(a, b, c):
    p = a * b * c
    print(f"The amount for 3 parameters  is : {p}")
    print("The amount you found is ".format(p))


# product(10, 1000) #  Uncommenting the below line shows an error(over_loaing)!

# This line will call the second product method
# product(4, 5, 5)
# Output:100

# Error:missing 1 required positional argument: 'c'
# product(4, 5)


# =================================================================================
# Function to take multiple arguments
def add(datatype, *args):  # sourcery skip: switch

    # if datatype is int:
    # initialize answer as 0
    if datatype == "int":
        answer = 0

    # if datatype is str:
    # initialize answer as ''
    if datatype == "str":
        answer = ""

    # Traverse through the arguments
    for item in args:

        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + item
    print(answer)

    # Integer
    # add('int', 5, 6)

    # String
    # add('str', 'Hi ', 'Geeks')


# Output:11
# Hi Geeks

# ================== pip3 install multipledispatch==========================================
"""
To Solve OverLoading in Python we use  @dispatch above our function
"""
from multipledispatch import dispatch

# By Using Multiple Dispatch Decorator
# passing one parameter
@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)


# passing two parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)


# you can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


# calling product method with 2 arguments
product(20, 5)  # Output:100
product(2, 3, 2)
#  output of :12
#  product(2.2,3.4,2.3)
#  output of :17.985999999999997
