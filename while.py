def multplication_tabele(n):
    for i in range(1, 11):
         print("{} X {} = {}".format(n, i, n*i))

n = input("Enter a number (0 to exit): ")
n = int(n)
        
while n != 0:
    multplication_tabele(n)
    print("")
    n = input("Enter a number (0 to exit): ")
    n = int(n)        