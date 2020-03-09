'''Program that reads two numbers and an
arithematical operation and display the
computed result'''

a = int(input("enter numbers only"))
b = int(input("enter numbers only"))

ch = input("")
if ch =='+':
    sum=a+b
    print("addition is",sum)
elif ch =="-":
    sum = a-b
    print("substraction is",sum)
elif ch =="*":
    sum = a*b
    print("multiplication is",sum)
elif ch =="/":
    sum = a/b
    print("division is",sum)
elif ch =="%":
    sum =a%b
    print("modulous is",sum)
else:
    print('''enter valid input "+  -  *  /  %"''')