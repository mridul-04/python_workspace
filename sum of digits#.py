n = int(input("enter a no"))
c = 0
while n !=0 :
    c+= n % 10
    n= n//10
print('sum of digits is:', c)
