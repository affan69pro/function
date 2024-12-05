def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("please select one option")
print("a to add")
print("b to substract")
print("c to multiply")
print("d to divide")

choice=(input("select a/b/c/d: "))

num1=float(input("PLease enter the first number: "))
num2=float(input("PLease enter the second number: "))

if choice==("a"):
    print(num1, "+", num2,"=", add(num1,num2) )
if choice==("b"):
    print(num1, "-", num2,"=", minus(num1,num2) )
if choice==("c"):
    print(num1, "x", num2,"=", multiply(num1,num2) )
if choice==("d"):
    print(num1, "/", num2,"=", divide(num1,num2) )
