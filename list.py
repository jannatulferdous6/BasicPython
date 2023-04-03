x = 200
print(isinstance(x, int))
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
thislist.insert(2, "water")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)