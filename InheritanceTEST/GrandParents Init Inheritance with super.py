class Meta:
    def __init__(self, meta_name):
        print('init Meta in')
        self.metaname = meta_name
        print('init Meta out')


class A(Meta):
    def __init__(self, nameA):
        print('init A in')
        super().__init__(nameA)
        self.nameA = nameA + "A"
        print('init A out')
    def funcA(self):
        print('func A '+ self.nameA)

class B(Meta):
    def __init__(self, nameB):
        print('init B in')
        super().__init__(nameB)
        self.nameB = nameB + "B"
        print('init B out')
    def funcB(self):
        print('func B '+ self.nameB)

class C(A, B):
    def __init__(self, name, sex):
        print(C.__mro__)
        print('init C in')
        # only one super needed since A and B are all inherited from Meta
        super().__init__(name)
        print('init C out')


c = C('myname', 'male')
# Using super to make mro BFS, like this
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Meta'>, <class 'object'>)

print(c.nameB)
c.funcA()
c.funcB()