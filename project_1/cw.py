# s=0
# for i in range(10):
#     a=int(input("Enter a number: "))
#     if a>0:
#         s=s+a
# print(s)   


# s,i=0,0
# while i<10:
#     a=int(input("Enter a number: "))
#     if a>0:
#         s+=a
#     i += 1
# print(s)

li=[]
i=1
while i<=5:
    a=int(input("Enter a number: "))
    li.append(a)
    i += 1
li.sort()
print(li)  