# Программа считает средний рост школьников по классам из TSV-файла.
# Формат каждой строки файла: "Класс Фамилия Рост" (через табуляцию),
# класс — число от 1 до 11, рост — натуральное число.
# Вывод: для каждого класса с 1 по 11 — средний рост как вещественное число,
# для классов без данных — прочерк "-".


lst = []
d = {}
path = r"dataset_3380_5.txt"
with open(path, "r", encoding='utf-8') as f:
    for line in f:
        lst.append(line.strip().split('\t'))
for i in lst:
    if int(i[0]) not in d:
        d[int(i[0])] = [0, 0]
    d[int(i[0])][0] += float(i[2])
    d[int(i[0])][1] += 1
with open('output.txt', "w", encoding='utf-8') as f:
    for i in range(1,12):
        if i in d:
            f.write(f"{i} {d[i][0]/d[i][1]}\n")
        else:
            f.write(f"{i}-\n")