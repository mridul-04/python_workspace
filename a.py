a=int(input("Enter a number: "))
for i in range(1, a+1):
    if a%i==0:
        print("The factors are",i )

a=int(input("Enter any number : "))
f=0
for i in range(2,a):
    if a%i==0:
        f+=1
if f == 0:
    print ("The number you have given is prime")
else:
    print ("The number you have given is composite")