def my_function(name):
  print(name + " khan")

my_function("Sajib")
my_function("Jahid")
my_function("Habib")
# #arguments
def my_function(name, lname):
  print(name + " " + lname)

my_function("Sajib", "khan")

# #*args
def my_function(*name):
  print(name[2])

my_function("sajib", "jahid", "rakib")

#key argument
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "jahid", child2 = "sajib", child3 = "rakib")

# #arbitrary key argument, **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "jahid ", lname = "hasan")

#default Parameter value

def my_function(name = "Jannat"):
  print(name)

my_function("Sajib")
my_function("Inaya")
my_function()
my_function("Sajib")

# passing a list as an argument

def my_function(fname):
  for x in fname:
    print(x)

name = ["jannat", "sajib", "jahid"]

my_function(name)

# Return value

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

## The pass Statement

def myfunction():
  pass