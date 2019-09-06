class Meta:
    def __init__(self, meta_name):
        print('init Meta in')
        self.metaname = meta_name
        print('init Meta out')

class A(Meta):
    def __init__(self, nameA):
        print('init A in')
        Meta.__init__(self, nameA)
        self.nameA = nameA + "A"
        print('init A out')
    def funcA(self):
        print('func A '+ self.nameA)

class B(Meta):
    def __init__(self, nameB):
        print('init B in')
        Meta.__init__(self, nameB)
        self.nameB = nameB + "B"
        print('init B out')
    def funcB(self):
        print('func B '+ self.nameB)

class C(A, B):
    def __init__(self, name):
        print('init C in')
        A.__init__(self, name)
        B.__init__(self, name)
        print('init C out')


c = C('myname')
c.funcA()
c.funcB()