a = float(input("Enter marks for Subject 1: "))
b = float(input("Enter marks for Subject 2: "))
c = float(input("Enter marks for Subject 3: "))
d = float(input("Enter marks for Subject 4: "))
e = float(input("Enter marks for Subject 5: "))

# Calculate total
total = a + b + c + d + e 

# Calculate average
average = total / 5

# Percentage calculation
percentage = (total / 500) * 100

# Display results
print("\nTotal Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage, "%")
