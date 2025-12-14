while True:
    s = input()
    print(s.upper())
    s = input("Do you want to continue? (type y to continue)")
    if s == "y":
        continue
    else:
        break
