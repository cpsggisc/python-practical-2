# Validating triangles and computing perimeter

side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

sum = side1 + side2

if sum > side3:
    perimeter = side1 + side2 + side3
    print("Perimeter =", perimeter)
else:
    print("Invalid triangle!")
