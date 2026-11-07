# Программа проверяет орфографию по списку известных слов.
# Входные данные:
#   d — количество известных слов, затем d строк со словами;
#   l — количество строк текста, затем l строк для проверки.
# Слова сравниваются без учёта регистра.
# Вывод: уникальные слова, отсутствующие в списке (в произвольном порядке).

s1 = []
s2 = []
res = set()
x = int(input())
for i in range(x):
    word = input()
    s1.append(word.lower())
y = int(input())
for i in range(y):
    word2 = input()
    s2.extend(word2.lower().split())
for i in s2:
    if i not in s1:
        res.add(i)
print('\n'.join(res))



