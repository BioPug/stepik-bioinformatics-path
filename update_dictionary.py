# Программа обновляет словарь d:
# - если key есть: добавляет value в список по этому ключу;
# - если key нет: использует ключ 2*key;
# - если 2*key тоже нет: создаёт запись {2*key: [value]}.
# Функция меняет словарь на месте, ничего не возвращает.

x = {}
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif (key * 2) in d:
        d[key * 2].append(value)
    else:
        d[key * 2] = [value]
update_dictionary(x,1,-3)
print(x)


