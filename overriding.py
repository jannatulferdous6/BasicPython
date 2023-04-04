class Phone:
    def __init__(self):
        print("i am in Phone class")

class Redmi(Phone):
    def __init__(self):
        super().__init__()
        print("i am in Redmi class")

r = Redmi()