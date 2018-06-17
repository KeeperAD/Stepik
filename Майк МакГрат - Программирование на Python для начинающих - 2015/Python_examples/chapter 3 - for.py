# str = 'Моя строка'
#
# for i in str:
#     print(i)

chars = ['A', 'B', 'C']
fruit = ('Яблоко', 'Банан', 'Вишня')
dict = {'name': ' Mike', 'ref': 'Python', 'sys': 'Win'}

print('\nElements:\t', end=' ')
for item in chars:
    print(item, end=' ')

print('\nEnumerate:\t', end=' ')
for item in zip(chars, fruit):
    print(item, end=' ')

print('\nPaired:')
for key, value in dict.items():
    print(key, '=', value)
