# Есть словарь песен группы Depeche Mode
# violator
#
songsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен, в название которых состоит из одного слова


print('\nОбщее время альбома: ', sum(songsdict.values()), ' минут\n')

spis = []
for key, value in songsdict.items():
    if value > 5:
        spis += (key, value)
print(spis)

new = {}
for key, value in songsdict.items():
    if ' ' not in key:
        new[key] = value
print(new)