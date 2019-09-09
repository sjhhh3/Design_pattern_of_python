class A:
    def __init__(self, name):
        self.name = name
        self.run()

    def __str__(self):
        return self.name + 'str'

    def __repr__(self):
        return self.name + 'repr'

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def run(self):
        print(self.name, "run")


a = A("apple")
b = A("apple")
print(a)
print(id(a))
print(a.__hash__())

print(b)
print(id(b))
print(b.__hash__())
print(hash("apple"))
print(hash("applerepr"))
print(a == b)
print(id(a) == id(b))

s = set()
s.add(a)
s.add(b)
print(s)