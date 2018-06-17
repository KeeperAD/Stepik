# a, b = (int(i) for i in input().split())

a = int(input())
b = int(input())

s = x = 0
for j in range(a, b + 1):
    if j % 3 == 0:
        s += j
        x += 1
print(s / x)
