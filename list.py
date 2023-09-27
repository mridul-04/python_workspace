f = ['hrithik','mridul']

for i in range(10):
    f.append(input("Enter a name: "))

print(type(f))
print(f)

for name in f:
    print(name)
    if name[0] == 'm':
        print(name, 'starts with m')
