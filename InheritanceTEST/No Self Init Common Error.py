class A:
    def __init__(self, name):
        self.nameA = name
        print('init A')
    def funcA(self):
        print('func A '+ self.nameA)

class B:
    def __init__(self, name):
        self.nameB = name
        print('init B')
    def funcB(self):
        print('func B '+ self.nameB)

class C(A, B):
    pass


''' 
    No self __init__ child, only passes the arguments to the very first parent which has __init__.
    Other parents take no arguments and no __init__ run.
'''
c = C('myname')
c.funcA()
c.funcB()