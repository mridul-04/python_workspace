# n=int(input("Enter the value of n: "))
# a,b,r=0,1,[0,1]
# for i in range(n-2):
#     c =(a+b)
#     a,b = b,c
#     r.append(c)
# print(r) 

n=int(input("Enter a number: "))
r=[0,1]
a,b=0,1
while True:
    c=(a+b)
    if(c>n): break
    r.append(c)
    a=b
    b=c
print(r)    