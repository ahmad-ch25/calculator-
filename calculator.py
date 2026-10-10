print("calculator")
value1 = int(input("enter first value "))
operations = input("+ - * / ")


def addition(first, second):
    global value2
    value2 = second
    add = first + second
    return add


def subtraction(first, second):
    global value2
    value2 = second
    sub = first - second
    return sub


def multiplication(first, second):
    global value2
    value2 = second
    multi = first * second
    return multi


def division(first, second):
    global value2
    value2 = second
    divide = first / second
    return divide


if operations == "+":
    value2 = int(input("enter second number "))
    print(addition(value1, value2))
if operations == "-":
    value2 = int(input("enter second value "))
    print(subtraction(value1, value2))
if operations == "*":
    value2 = int(input("enter second value "))
    print(multiplication(value1, value2))
if operations == "/":
    value2 = int(input("enter second value "))
    print(division(value1, value2))
