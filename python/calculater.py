first = float(input("enter first number: "))
second = float(input("enter second number: "))
opr = str(input("enter operation (+, -, *, /): "))

if opr == "+":
    total = first + second
elif opr == "-":
    total = first - second
elif opr == "*":
    total = first * second
elif opr == "/":
    total = first / second
else:
    total = str("please enter a valid operation")

print(total)
