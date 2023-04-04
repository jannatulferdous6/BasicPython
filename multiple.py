class A: 
    def display(self):
        print("i am inside A clas")

class B(): 
    def display(self):
        print("i am inside B clas")

class C(A,B):
    pass

c1 = C()
c1.display()