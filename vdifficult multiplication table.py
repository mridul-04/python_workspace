num1 = int(input("enter the starting point -: "))
num2 = int(input("enter the ending point -: "))
print(" The multiples are : ")
for i in range(num1, num2):
    if 0 == i % 12:
        print(i)
