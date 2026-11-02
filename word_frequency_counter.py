# Программа читывает одну строку текста,
# подсчитывает частоту каждого слова (без учёта регистра),
# выводит уникальные слова и количество их повторений
# в формате «слово количество».

lst = [str(i) for i in input().lower().split()]
d = {}
for i in lst:
    val = lst.count(i)
    if i not in d:
        d[i] = [val]
for key, value in d.items():
    print(key,*value)