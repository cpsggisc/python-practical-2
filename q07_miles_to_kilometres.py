# Conversion from miles to kilometres

print("Miles\tKilometers\tKilometers\tMiles")

for i in range(0,10):
    print("{0}\t{1:.3f}\t\t{2}\t\t{3:.3f}\t\t".format(i+1, (i+1)*1.609, i*5 + 20, (i*5 + 20)/1.609))
