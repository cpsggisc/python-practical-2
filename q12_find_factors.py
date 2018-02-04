# Finding the factors of an integer

num = int(input("Enter integer: "))
i = 2

if num == 1:
    print("1")
else:
    while num >= i:
        if num % i == 0:
            print(i)
            num = num / i
        else:
            i = i + 1

