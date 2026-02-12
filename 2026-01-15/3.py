# является ли число n простым
n = int(input())
if n == 1:
    print('no')
    exit(0)
d = 2
while d**2 <= n:
    if n % d == 0:
        print('no')
        break
    d += 1
else:
    print('yes')