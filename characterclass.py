import re
pattern = r"[aeiou]"
if re.match(pattern,"advbakksnceuuycds"):
    print("match")

if re.match(pattern,"gghhyyttrrppss"):
    print("match")

pattern = r"[A-z]"
if re.match(pattern,"Aggghhh"):
    print("matched")

pattern = r"[0-9]"
if re.match(pattern,"0Agg1gh2hh"):
    print("matched")

pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern,"Ag1gh2hh"):
    print("matched")