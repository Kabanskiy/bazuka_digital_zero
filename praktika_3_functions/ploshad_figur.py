# В зависимости от выбора пользователя вычислить площадь круга, прямоугольника или треугольника.
# Для вычисления площади каждой фигуры должна быть написана отдельная функция

import math

def krug(r):
    return(math.pi * r ** 2)
def pryam(a, b):
    return(a * b)
def treug(a, b, c):
    pp = (a+b+c)/2 # полупериметр
    return math.sqrt (pp*(pp-a)*(pp-b)*(pp-c)) # math.sqrt находит корень квадратный выражения. И находится по формуле

figura = input('Выбери фигуру: 1 - круг, 2 - прямоугольник, 3 - треугольник: ')

if figura == '1':
    r = int(input('Введи радиус: '))
    s = krug(r) # помещаем в переменную s
    print(f'Площадь круга с радиусом {r} равна {s}')
elif figura == '2':
    a = int(input('ВВеди первую сторону прямоуг: '))
    b = int(input('ВВеди вторую сторону прямоуг: '))
    s = pryam(a, b)
    print(f'Площадь прямоугольника со сторонами {a} и {b} равна {s}')
else:
    a = int(input('введи первую сторону треугольника: '))
    b = int(input('введи вторую сторону треугольника: '))
    c = int(input('введи третью сторону треугольника: '))
    s = treug(a, b, c)
    print(f'Площадь треугольника со сторонами {a} , {b}, {c} равна {s}')