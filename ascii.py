char = input("Enter a character: ")
if len(char) == 1:
    ascii_value = ord(char)
    print("The ASCII value of", char, "is", ascii_value)
else:
    print("Please enter only a single character.")