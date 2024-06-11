#WAP to take 10 numbers from user and print the largest number

list_1=[]
print("Enter 10 numbers: ")
for i in range(10):
    a=int(input(""))
    list_1.append(a)
print(list_1)
max=0
for i in range(10):
    if list_1[i]>=max:
        max=list_1[i]
print(max)

