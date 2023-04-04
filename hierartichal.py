class A: 
    def display(self):
        print("i am inside A clas")

class B(A): 
    def display(self):
        print("i am inside B clas")

class C(A): 
    def display(self):
        print("i am inside C clas")

b1 = B()
b1.display()

c1 = C()
c1.display()