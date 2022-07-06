"""
Practise Generators in Python
Yields: Returns amount of value
"""
# Python - Generator Functions
# test generator


def mygenerator():
    """
    create your own iterator function.,,,,i
    returns an iterator object

    Yields:instead of Return but here it makes a Pause
    """
    print("First item")
    yield 10

    print("Second item")
    yield 20

    print("Last item")
    yield 30


#  python -m pycodestyle ./generator_func.py
# gen = mygenerator()
# next(gen)
# next(gen)
# next(gen)

# ===========================================================
"""
Using for Loop with Generator Function
"""
def square_of_sequence(my_numb):
    for i in range(my_numb):
        yield i*i
        next(seq)
        yield i*i
    print("DONE")
        # seq = square_of_sequence(5)



def get_sequence_upto(my_numb):  # sourcery skip: yield-from

    for i in range(my_numb):
     yield i


seq = get_sequence_upto(5)
next(seq)
next(seq)
next(seq)


squres=(x*x for x in range(5))
print(next(squres))
