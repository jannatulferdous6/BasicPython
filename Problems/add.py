num1 = input("first number: ")
num2 = input("Second Number: ")

sum = float(num1) + float(num2)
print(sum)

if __name__ == "__main__":
    
              num3 = 15
              num4 = 3
              sum_twoNum = lambda num3, num4 : num3 + num4
              print(sum_twoNum(num3, num4))


def add(a,b):
        return a+b
num1 = 12
num2 = 12
sum_twoNum = add(num1, num2)
print(sum_twoNum)


num1 = 12
num2 = 12
import operator
sum1 = operator.add(num1, num2)
print(sum1)