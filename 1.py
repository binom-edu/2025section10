def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print('В подпрограмме:', a)

a = int(input())
b = int(input())
gcd(a, b)
print('В основном коде:', a)