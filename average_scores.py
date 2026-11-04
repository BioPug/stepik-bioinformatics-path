# Программа читает файл со строками вида "Фамилия;Математика;Физика;Русский".
# Для каждого абитуриента считает средний балл по трём предметам и пишет его в выходной файл.
# В последней строке — средние баллы по каждому предмету среди всех абитуриентов.

lst = []
first = 0
second = 0
third = 0
student = 0
path = r"dataset_3363_4.txt"
with open(path, "r", encoding='utf-8') as f:
    for line in f:
        l = line.strip().split(';')
        lst.append(l)
with open('output.txt', "w", encoding='utf-8') as f:
    for l in lst:
        first += float(l[1])
        second += float(l[2])
        third += float(l[3])
        student += 1
        avr_student = (float(l[1])+float(l[2])+float(l[3]))/3
        f.write(str(avr_student)+'\n')
    sum_first = first/student
    sum_second = second/student
    sum_third = third/student
    res = [str(sum_first),str(sum_second),str(sum_third)]
    f.write(' '.join(res))



