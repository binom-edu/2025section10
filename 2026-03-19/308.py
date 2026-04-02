def f(x,y):
    return x != y

x, y = map(int, input().split())
print(int(f(x, y)))