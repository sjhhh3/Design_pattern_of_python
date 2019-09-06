'''
1. What will happen if class variables of two parents are with same name?
    Answer: Get the leftest
2. isinstance testing for multi-inheritance
3. issubclass testing for multi-inheritance
4. staticmethod/classmethod/property inheritance

'''

class Meta:
    metadata = 50
    def __init__(self):
        self.number_for_property_use = 10

    @staticmethod
    def stamt():
        return f'static method get number {5}'

    @classmethod
    def clsmt(cls):
        return f'class method get number {cls.metadata}'

    @property
    def prop(self):
        return f'property get number {self.number_for_property_use + 1}'

class A(Meta):
    classv = 1

class B(Meta):
    classv = 2

class C(A, B):
    pass

c = C()
print(c.classv)
print(c.metadata)
print(c.stamt())
print(c.clsmt())
print(c.prop)

print(isinstance(c, A))
print(isinstance(c, B))
print(isinstance(c, C))
print(isinstance(c, object))
print(issubclass(C, A))
print(issubclass(C, B))
print(issubclass(C, Meta))
print(issubclass(C, object))