n = input()
n = int(n)
if n>=0:
    print("Positive")
else:
    print("Negative")
"""
if n % 2 ==0:
    print("Even")
else:
    print("Odd")
    """
if n>=0 and n % 2 == 0:
        print("Positive Even")
    elif n>=0 and n % 2 == 1:
        print("Positive Odd")
elif n<0 and n %2==0:
        print("Negative Even")
    else:
        print("Negative Odd")
