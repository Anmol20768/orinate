class A:

    def __init__(self, a):
        self.a=a

    def __lt__(self,other):
        if (self.a < other.a):
            print("obj1 is less then obj2")

        else:
            print("obj2 is less then obj1")

    def __eq__(self,other):
        if (self.a == other.a):
            print("they are equal")

        else:
            print("they arent equal")

obj1 = A(1)
obj2 = A(2)
print("value passed:", obj1.a, obj2.a)
print(obj2 < obj1)

obj1 = A(2)
obj2 = A(2)
print("value passed:", obj1.a, obj2.a)
print(obj2 == obj1)