def minimum(a, b, c, d):
    ans = a
    if b < ans:
        ans = b
    if c < ans:
        ans = c
    if d < ans:
        ans = d
    return ans

a, b, c, d = map(int, input().split())
print(minimum(a, b, c, d))