s=0
for i in range(10):
    a=int(input("Enter a number: "))
    if a>0:
        s=s+a
print("The sum of numbers is",s)   

s,i=0,0
while i<10:
    a=int(input("Enter a number: "))
    if a>0:
        s+=a
    i += 1
print("The sum of numbers is",s)