n=int(input("enter a number"))
c,z=0,n
while n !=0:
    d = n%10
    c = c + (d**3)
    n=n//10
if c == z:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
