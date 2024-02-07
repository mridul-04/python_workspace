# a = [1, 3, 2, 5, 6]
# odd,even=0,0

# for i in a:
#     if i%2==0:
#         even+=1
#     else:    
#         odd+=1
# print("The number of odd numbers are",odd)    

# print("The number of even numbers are",even)    

# a = int(input("Enter 1st number"))
# b = int(input("Enter 2nd number"))
# c = int(input("Enter 3rd number"))

# if a > b and a > c:
#     print(a)

# elif b > a and b > c:
#     print(b)

# elif c > a and c > b:
#     print(c)

# else:
#     print('Numbers are same')


# if a < b and a < c:
#     print(a)

# elif b < a and b < c:
#     print(b)

# elif c < a and c < b:
#     print(c)

# else:
#     print('Numbers are same')

# jan january JANUARY January 
# n = int(input("Enter \n1. for Jan \n2. for Feb \n3. for Mar "))
# if n == 1 or n == 3 or n == 5 or n == 7  or n == 8  or n == 10  or n == 12:
#     print("31 days")
# elif n == 2:
#     print("28 or 29 days")
# else:
#     print("30 days")


# a = "qwarty123"
# d,l = 0,0
# for i in a:
#     if(i.isdigit()):
#         d += 1
#     if (i.isalpha()):
#         l += 1

# print("Digit", d)
# print("Letters", l)

# a = []
# for i in range(10):
#     x=int(input("Enter list: "))
#     a.append(x)

# print(a)
# p=0
# for i in a:
#     if i%3==0:
#         p=p+1

# print(p)


# for i in range(700,6,-7):
#     print(i)


a = "rfaaewflj43fes287"
i = 0
while i < len(a):
    if a[i].isalpha():
        print(a[i])
    i += 1