"""
Using Super(): Python super() function provides us the facility to refer
to the parent class explicitly. It is basically useful where we have to call
superclass functions. It returns the proxy object that allows us to refer parent class by super.

 """
class SGS1:
    def __init__(self):
        print("PART1 DONE")

    def sub_SGS(self, b):
        print("sub sgs 2 ready", b)


class SGS2(SGS1):
    def __init__(self):
        print("PART2 DONE")
        super().__init__()

    def sub_SGS(self, b):
        print("sub sgs 2 ready", b)
        super().sub_SGS(b)


class SGS3(SGS2):
    def __init__(self):
        print("PART3 DONE")
        super().__init__()

    def sub_SGS(self, b):
        print("sub sgs 2 ready", b)
        super().sub_SGS(b)


sgs = SGS3()
sgs.sub_SGS(15)
