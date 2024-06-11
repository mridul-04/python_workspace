n=int(input("Enter any number: "))
k , z= 0, n
while n !=0:
    m=n%10
    c = 1
    for i in range(1,m+1):
        c = c * i
    k += c
    n = n // 10
if k == z:
    print('Krishnamurty number')
else:
    print('Not a krishnamurty number')