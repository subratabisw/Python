def generate_multiplication_table(n):
    for i in range(1, n + 1):
        print(f"{n} x {i} = {n * i}")

n = int(input("Please enter a number: "))

# Call the function
generate_multiplication_table(n)

