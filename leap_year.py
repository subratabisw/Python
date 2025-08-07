year = int(input("Enter a year: "))
result = "Leap Year" if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else "Not a Leap Year"
print("The year is:", result)