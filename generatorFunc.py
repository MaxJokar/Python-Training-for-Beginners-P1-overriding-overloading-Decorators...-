
# Python - Generator Functions
# test generator

def mygenerator():
    """create your own iterator function.,,,,i
     returns an iterator object

    Yields:
        _type_: _description_
    """
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30




# gen=mygenerator()
# next(gen)
# next(gen)
# next(gen)


# Using for Loop with Generator Function

def square_of_sequence(x):
    for i in range(x):
        yield i*i


seq = square_of_sequence(5)
next(seq) 
 






def get_sequence_upto(x):  # sourcery skip: yield-from
    for i in range(x):
        yield i



# seq = get_sequence_upto(5)
# next(seq) 
# next(seq) 
# next(seq) 





# squres = (x*x for x in range(5))
# print(next(squres)) 










