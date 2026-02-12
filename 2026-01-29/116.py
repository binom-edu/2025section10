n = int(input())

mn = 10
while n > 0:
    d = n % 10
    if d < mn:
        mn = d
    n //= 10
print(mn)