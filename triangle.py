a = float(input("Enter first angle:"))
b = float(input("Enter second angle:"))
if a + b > 180:
    print("The angles don't form a triangle.")
else:
    c = 180 - (a +b)
    print("The third angle is:", c)