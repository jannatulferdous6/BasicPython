# # reading a file
# file = open("Student.txt", "r")
# print(file.readable())
# file.close()

# file = open("Student.txt", "w")
# print(file.writable())
# file.close()

# # # from Student.txt file
# file = open("Student.txt", "r+")
# text = file.read()
# print(text)
# size = len(text)
# print(size)

# text = file.readlines()[1]
# print(text)
# file.close()

# #writing in a file

file = open("Student.txt", "r+")

file.write("\n Sadi - lectuer of physics")
file.close()