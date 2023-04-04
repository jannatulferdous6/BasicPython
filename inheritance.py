class Phone:
    def call(self):
        print("you can call")
    def message(self):
        print("ou can message")

class Redmi(Phone):
    def photo(self):
        print("you can photo")

r = Redmi()
r.call()
r.message()
r.photo()
print(issubclass(Redmi, Phone))