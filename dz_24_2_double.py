# Проверить, есть ли в последовательности чисел списка дубликаты

a = [2, 3, 95, 4, 7, 10, 2]
new_set = set(a)

if len(new_set) == len(a):
    print('Дубликатов нет')
else:
    print('Дубликаты есть')