def area_perimeter(l, b):
    return l * b, 2 * (l + b), ((l * l) + (b * b)) ** .5


l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
c = area_perimeter(l, b)
print(c[::-1])


def sum_numbers(a, b, c):
    return a + b + c


a = int(input("Enter the First number: "))
b = int(input("Enter the Second number: "))
c = int(input("Enter the Third number: "))
print(sum_numbers(a, b, c))


def numbers(a, b, c):
    if a < b < c:
        return a, b, c
    if a < c < b:
        return a, c, b
    if b < a < c:
        return b, a, c
    if b < c < a:
        return b, c, a
    if c < a < b:
        return c, a, b
    if c < b < a:
        return c, b, a


a = int(input("Enter the First number: "))
b = int(input("Enter the Second number: "))
c = int(input("Enter the Third  number: "))
print(numbers(a, b, c))


