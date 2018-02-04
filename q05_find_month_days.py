# Finding the number of days in a month

month = int(input("Enter month: "))
year = int(input("Enter year: "))


monthname = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthlength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # leap year
    monthlength[1] = 29

print("{0} {1} has {2} days.".format(monthname[month-1],year,monthlength[month-1]))
