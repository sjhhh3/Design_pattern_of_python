class A:
    def __init__(self, name):
        self.name = name
        print('init A')
    def func(self):
        print('func A '+ self.name)

class B:
    def __init__(self, name):
        self.name = name
        print('init B')
    def func(self):
        print('func B '+ self.name)

class C(A, B):
    pass


''' 
    Parents' regular methods with same name, only pick the leftest when run "c.func()".
    If want to get the func from specific parent, use B.func(c).
'''
c = C('myname')
c.func()
B.func(c)
