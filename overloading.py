
# First product method.
# Takes two argument and print their
# product

def product(a, b):
    """in Python :The problem with method overloading  is that
    we may overload the methods but can only use the "latest defined method". 
    """
    p = a * b
    print(p)
      
# Second product method
# Takes three argument and print their
product
def product(a, b, c):
    p = a * b*c
    print(p)
  
# Uncommenting the below line shows an error    
# product(4, 5)
  
# This line will call the second product method
# product(4, 5, 5)
#Output:100

#Error:missing 1 required positional argument: 'c'
# product(4, 5)


#=================================================================================


# Function to take multiple arguments
def add(datatype, *args):  # sourcery skip: switch
  
    # if datatype is int
    # initialize answer as 0
    if datatype =='int':
        answer = 0
          
    # if datatype is str
    # initialize answer as ''
    if datatype =='str':
        answer =''
  
    # Traverse through the arguments
    for x in args:
  
        # This will do addition if the 
        # arguments are int. Or concatenation 
        # if the arguments are str
        answer = answer + x
  
    print(answer)
  
# Integer
# add('int', 5, 6)
  
# String
# add('str', 'Hi ', 'Geeks')



#Output:11
# Hi Geeks

#================== pip3 install multipledispatch==========================================

from multipledispatch import dispatch
 
#By Using Multiple Dispatch Decorator  
#passing one parameter
@dispatch(int,int)
def product(first,second):
    result = first*second
    print(result)
  
#passing two parameters
@dispatch(int,int,int)
def product(first,second,third):
    result  = first * second * third
    print(result)
  
#you can also pass data type of any value as per requirement
@dispatch(float,float,float)
def product(first,second,third):
    result  = first * second * third
    print(result)
  
  
#calling product method with 2 arguments
# product(20,5)        Output:100
# product(2,3,2)
#                      output of :12
# product(2.2,3.4,2.3) 
#                     output of :17.985999999999997









