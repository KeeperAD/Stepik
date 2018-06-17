# a, b = int(input()), int(input())
# i = a * b
# nod = 1
#
# while i >= 1:
#     if i % a == 0 and i % b == 0:
#         nod = i
#     i -= 1
# print(nod)


a = int(input())
b = int(input())
x = 1
while (x % a != 0) or (x % b != 0):
    x += 1

print(x)
