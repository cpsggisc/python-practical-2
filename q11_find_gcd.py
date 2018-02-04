# Computing the greatest common divisor

n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))

if n1 > n2:
    d = n2
    while n1 % d != 0 or n2 % d != 0:
        d -= 1
    print("The greatest common divisor of both integers is", d)
else:
    d = n1
    while n2 % d != 0 or n1 % d != 0:
        d -= 1
    print("The greatest common divisor of both integers is", d)
