try:
   list = [20, 0, 30]
   result = list[0] / list[3]
   print(result)
   print("Done")
except ZeroDivisionError:
   print("Dividing by zero is not possible")
except IndexError:
   print("Index error")

print("Successful")

#finally:

try:
  list = [20, 0, 30]
  result = list[0] / list[3]
  print(result)
  print("Done")
except ZeroDivisionError:
  print("Dividing by zero is not possible")
finally: 
  print("Successful")

try: 
  num1 = int(input("1st number: "))
  num2 = int(input("2nd number: "))
  result = num1/ num2
  print(result)
except (ValueError, ZeroDivisionError):
    print("you have entered incorrect input")
finally:
    print("thanks")
 
# def voter(age):
#    if age < 18:
#      raise ValueError("Invalid Voter")
#    return "You are allowed to vote"
# try:
#   print(voter(19))
#   print(voter(16))
# except ValueError as e:
#    print(e)