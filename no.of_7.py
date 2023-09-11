a=int(input("Enter any number : " ))
c=0
while a!=0: 
    h=a%10
    if h==7:
        c+=1
    a=a//10
print (c)