n, m, k = map(int, input().split())

# вычисляем сколько работ нужно проверить всем сеньорам
total_reviews = n * k

# вычисляем сколько минут потребуется для проверки всех работ
time_required = (total_reviews + m - 1) // m

# выводим результат
print(time_required)