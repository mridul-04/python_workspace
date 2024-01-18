from datetime import datetime
a=int(input("Enter the starting point: "))
b=int(input("Enter the ending point: "))
c=int(input("Enter the number who's factors needs to be printed: "))
s = 0
t1=datetime.now()
if a%c != 0:
    a = a - (a%c) + c


#efficient one
for i in range(a,b+1,c):
    s += i
    print(i)
print(datetime.now()-t1)
t1=datetime.now()

#in efficient one
for i in range(a,b+1):
    if i % c == 0:
        s += i
        print(i)
print(datetime.now()-t1)

# 0:00:00.156613
# 0:00:00.192518