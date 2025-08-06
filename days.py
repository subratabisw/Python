a = float(input("Enter the number of days:"))
years = a// 365
remaining_days = a % 365
weeks = remaining_days // 7
days = remaining_days % 7
print("Years:", years)
print("Weeks:", weeks)
print("Days:", days)

