import re
pattern = r"Red"
# if re.match(pattern, "Red is a Colour"):
#     print("match")
# else:
#     print("not match")


# if re.search(pattern,"Red is a colour"):
#     print("Match")
# else:
#     print("Not match")

# print(re.findall(pattern, "Red is a colour, Red is  my favoriate"))

text = "my favourite colour is Red"
match = re.search(pattern, text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())