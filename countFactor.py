# m = int(input("Enter a number: "))
# c = 0
# for i in range(1,m+1):
#         if m%i == 0 :
#             c += 1
# print('The number of factors of',m,'are',c)




a=int(input("Enter a number: "))
c=0
for i in range(1,a+1):
    if a%i==0:
        c+=1
if c==2:
    print('Prime Number')    
else:
    print('Composite number')            
              

