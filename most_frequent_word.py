# Программа ищет самое частое слово в тексте (файл может содержать несколько строк).
# Слова в разных регистрах считаются одинаковыми.
# Если несколько слов встречаются одинаково часто, выводим лексикографически первое.
# Вывод: слово и через пробел — количество вхождений.

lst = []
d = {}
path = r
with open(path, "r", encoding='utf-8') as f:
    for line in f:
        for word in line.lower().split():
            lst.append(word)
for word in lst:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
freq = max(d.values())
best_word = min([k for k,v in d.items() if v == freq])
print(best_word, freq, end=' ')


