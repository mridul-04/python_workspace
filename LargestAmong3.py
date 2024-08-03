def largestAmong3(a, b, c):
    if a> b and a > c:
        return a
    elif b> c and b> a:
        return b
    elif c>b  and c > a:
        return c
    else:
        return "All Numbers are same"

a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))

print(largestAmong3(a, b, c))

