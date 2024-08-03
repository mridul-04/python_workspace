def is_equable(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area == perimeter


a = int(input("Enter the first value"))
b = int(input("Enter the second value"))
c = int(input("Enter the third value"))
print(is_equable(a,b,c))
