# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
# Создайте множество цветов, произрастающих одновременно в саду и на лугу

print(set(garden) & set(meadow)) # Если имеется ввиду одинаковые виды

print(set(garden) | set(meadow)) # Если имеется ввиду все виды цветов


