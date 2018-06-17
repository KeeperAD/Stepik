print()
print()
dict = {'name': 'Bob', 'ref': 'Python', 'sys': 'Win'}
print('Dictionary:', dict)
print()
print()
print('Reference:', dict['ref'])
print()
print()
print('Keys:', dict.keys())
print()
print()
del dict['name']
dict['user'] = 'Tom'
print('Dictionary:', dict)
print()
print()
print('Is There A name key?:', 'name' in dict)

