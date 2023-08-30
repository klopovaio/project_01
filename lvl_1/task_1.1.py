# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
print (my_favorite_songs[0:14]) # 1 trek
print (my_favorite_songs[64:]) # last trek
print (my_favorite_songs[16:23]+my_favorite_songs[24:30]) # 2 trek
print (my_favorite_songs[51:-15]) # prelast trek