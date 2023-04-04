class A: 
    def display(self):
        print("i am inside A clas")

class B(A): 
    def display1(self):
        print("i am inside B clas")

class C(B): 
    def display2(self):
        super().display()
        super().display1()
        print("i am inside C clas")

c1 = C()

c1.display2()
