while True:
    n1 = int(input("first Number: "))
    n2 = int(input("second number:"))
    if n1 == 0 and n2 == 0:
        break
    try:
        print("Result:" , n1/n2)
    except ZeroDivisionError:
        print("Can't divide by 0")
    else:
        print("Goood Job!")
