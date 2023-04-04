import re 
# pattern = r"colo.r"

# if re.match(pattern,"colour"):
#     print("matched")

# pattern = r"(ab)*"

# if re.match(pattern, "abaaacolour"):
#     print("matched")

# pattern = r"a+"

# if re.match(pattern, "aaksngr"):
#     print("matched")

# pattern = r"a+b"

# if re.match(pattern, "abcoloraksngr"):
#     print("matched")

# pattern = r"ice(-)?cream"

# if re.match(pattern, "ice----cream"):
#     print("matched")

pattern = r"a{1,3}$"

if re.match(pattern, "aaa"):
    print("matched")