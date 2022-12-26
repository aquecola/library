english = {
    'рука': 'hand',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'back-end developer'
}

print(english['хвост'])

old_letters = {
    'ять': 'Ѣ',
    'юс малый': 'Ѧ',
    'юс большой': 'Ѫ'}

print(old_letters.values()) # Будет напечатан список значений словаря

favorite_songs = {
    'Тополиный пух': 'Иванушки international',
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино'
}

print(favorite_songs.keys()) # Будет напечатан список ключей словаря
                             # dict_keys(['Тополиный пух', 'Город золотой', 'Звезда по имени Солнце'])

favorite_songs = {
    'Тополиный пух': 'Иванушки international',
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино',
    'Space Oddity': 'David Bowie',
    'Рыба': 'Аквариум',
    'Серенада Трубадура': 'Муслим Магомаев',
}

for song, performer in favorite_songs.items():
	print('Песню ' + song + ' исполняет ' + performer) #method items

friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

# Объявлен пустой словарь, его нужно будет наполнить элементами, 
# каждый из которых составлен по схеме "имя: город"
friends =  {}

# Допишите ваш код сюда
for i in range(0, len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]

print('Лена живёт в городе ' + friends['Лена'])

favorite_songs = {
    'Серёга': ['Unforgiven', 'Holiday', 'Highway to hell'], 
    'Соня': ['Shake it out', 'The Show Must Go On', 'Наше лето'], 
    'Дима': ['Владимирский централ', 'Мурка', 'Третье сентября']
}

print(len(favorite_songs['Дима'])) #возвращает число элементов из списка.

for songs in favorite_songs['Соня']:
    print(songs)