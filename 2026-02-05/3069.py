prev = int(input())
ans = 0
while (x := int(input())) != 0:
    if x > prev: ans += 1
    prev = x

print(ans)