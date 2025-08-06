# Integer
int_val = int(input("Enter an integer: "))
print("You entered integer:", int_val)

# Float
float_val = float(input("Enter a float: "))
print("You entered float:", float_val)

# String
str_val = input("Enter a string: ")
print("You entered string:", str_val)

# Boolean
bool_input = input("Enter a boolean value (True/False): ")
bool_val = bool_input.lower() == 'true'
print("You entered boolean:", bool_val)

# Complex
real_part = float(input("Enter real part of complex number: "))
imag_part = float(input("Enter imaginary part of complex number: "))
complex_val = complex(real_part, imag_part)
print("You entered complex number:", complex_val)

