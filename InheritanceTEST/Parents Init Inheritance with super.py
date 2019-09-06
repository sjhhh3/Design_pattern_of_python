class A:
    def __init__(self, nameA):
        print('init A in')
        # all super(type, obj).func() calls the next callable func() in MRO order, not type's parent
        super().__init__(nameA)
        self.nameA = nameA + "A"
        print('init A out')
    def funcA(self):
        print('func A '+ self.nameA)

class B:
    def __init__(self, nameB):
        print('init B in')
        # this super takes no argument since next class in MRO order is "object"
        super().__init__()
        self.nameB = nameB + "B"
        print('init B out')
    def funcB(self):
        print('func B '+ self.nameB)

class C(A, B):
    def __init__(self, nameC):
        print(C.__mro__)
        super().__init__(nameC)

c = C("myname")
print(c.nameA)
print(c.nameB)
c.funcA()
c.funcB()

