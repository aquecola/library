DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Кто все мои друзья?':
        for friend in DATABASE:
            friends_string = friend + '.'
            return('Твои друзья: ' + friends_string)

print(process_anfisa('Кто все мои друзья?'))
print("*")

for friend in DATABASE:
                friends_string = friend + ' '
                print('Твои друзья: ' + friends_string)