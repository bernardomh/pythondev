print("Hello World")
#input("Enter your input")
try:
    mode=int(input("Input:"))
except ValueError:
    print("Not a number")
print("The input is",mode)

cond1= mode>10
cond2= mode>12
if cond1 and cond2:
    print(mode,"greater than 10 and 12")
else:
    print(mode,"smaller than 10 and 12")


