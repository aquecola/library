def print_valid_cities(all_cities, used_cities):
    diff = all_cities.difference(used_cities)
    for city in diff:
        print(city)


def add_cities(all_cities, new_cities):
    N=0
    for new_list in new_cities:
    
        all_cities.add(new_cities[N])
        if N==5:
            break
        else:
            N=N+1
            return add_cities

        
        



#def comfort_count(temperatures):
#    # Напишите код функции
#    N=0
#    for temp in temperatures:
#        if temp >= 22 and temp <= 26:
#            N = N + 1
#    print('Количество тёплых дней в этом месяце:', N)

#N=0
#for new_list in thisset2:
#    thisset.add(thisset2[N])
#    if N==1:
#        break
#    else:
#        N=N+1
    


new_cities = [
    'Екатеринбург',
    'Выборг' ,
    'Владивосток',
    'Казань',
    'Why',
    'Йезд'
]

all_cities = {
    'Абакан',
    'Астрахань', 
    'Бобруйск', 
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк', 
    'Новосибирск'
}

used_cities = {
    'Калуга',
    'Абакан' ,
    'Новосибирск'
}

add_cities(all_cities, new_cities)
print_valid_cities(all_cities, used_cities)