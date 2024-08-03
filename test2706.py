#list_1 = []

# a = int(input("Enter the number off which the table needs to be printed"))
# for i in range(1,11,1):
#     list_1.append(i*a)
# print(list_1)

# a = int(input("Enter the starting point: "))
# b = int(input("Enter the ending point: "))
# for i in range(a, b):
#     c = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             c += 1
#     if c == 2:
#         list_1.append(i)
#
# print(list_1)

# a=int(input("Enter any number"))
# while a!=0:
#     b=a%10
#     list_1.append(b)
#     a=a//10
# list_1 = list_1[::-1]
# print(list_1)

#
# count=0
# for i in range(10):
#     a=int(input("Enter numbers"))
#     if a%8==0:
#         count+=1
# print(count)

a=0
b=0
list_1 = []
list_2=[]
for i in range(100):
    d=int(input("Enter a number"))
    if d%2==0:
        a+=d
        list_1.append(d)
    else:
        b+=d
        list_2.append(d)

