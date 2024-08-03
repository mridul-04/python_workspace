# 17

def is_prime(n):
    f = 0
    for i in range(1, n + 1):
        if n % i == 0:
            f += 1

    if f == 2:
        return True
    else:
        return False


def reverse(n):
    r = 0
    while n > 0:
        b = n % 10
        r = r * 10 + b
        n //= 10
    return r


a = int(input("Enter a number: "))

if is_prime(a):
    r = reverse(a)
    if is_prime(r):
        print("Twin Prime")
    else:
        print("Prime But not twin Prime")

else:
    print("Composite Number")

