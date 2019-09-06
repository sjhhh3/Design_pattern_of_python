class MetaA:
    def __init__(self, meta_name):
        print('init MetaA in')
        self.metaname = meta_name
        print('init MetaA out')

class MetaB:
    def __init__(self, meta_name):
        print('init MetaB in')
        self.metaname = meta_name
        print('init MetaB out')

class A(MetaA):
    def __init__(self, nameA):
        print('init A in')
        super().__init__(nameA)
        self.nameA = nameA + "A"
        print('init A out')
    def funcA(self):
        print('func A '+ self.nameA)

class B(MetaB):
    def __init__(self, nameB):
        print('init B in')
        super().__init__(nameB)
        self.nameB = nameB + "B"
        print('init B out')
    def funcB(self):
        print('func B '+ self.nameB)

class C(A, B):
    def __init__(self, name):
        print('init C in')
        super().__init__(name)
        # if not include following B.__init__, the B.__init__ will never be called
        B.__init__(self, name)
        print('init C out')


c = C('myname')
# Since A from MetaA, B from MetaB, mro tree is like this
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.MetaA'>, <class '__main__.B'>, <class '__main__.MetaB'>, <class 'object'>)
print(C.__mro__)
# print(c.nameB)
# c.funcB()
# c.funcB()