# colors_tuple = ('Red', 'Green', 'Red', 'Blue', 'Red')
# a, b, c, d, e = colors_tuple
# print(a, b, c, d, e, sep='\n')

print()
print()
zoo = ('Кенгура', 'Леопард', 'Мышь')
print('Кортеж', zoo, '\tДлинной:', len(zoo))
print(type(zoo))
print()
print()

bag = {'Красный', 'Зеленый', 'Голубой'}
bag.add('Желтый')
print('Множество', bag, '\tДлинной:', len(bag))
print(type(bag))
print()
print()

print('Зеленый есть в множестве bag?', 'Зеленый' in bag)
print('Оранжевый есть в множестве bag?', 'Оранжевый' in bag)
print()
print()

box = {'Красный', 'Пурпурный', 'Желтый'}
print('Множество', box, '\tДлинной:', len(box))
print('Общее для множеств bag и box:', bag.intersection(box))
