a = float(input("Enter first float:"))
b = float(input("Enter second float:"))
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
if b!= 0:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
else:
    print("Division, Floor Division and Modulus: Not possible (division by zero)")
print("Exponentiation:", a ** b)
