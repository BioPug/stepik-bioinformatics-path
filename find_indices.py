#Программа, которая считывает список чисел из первой строки и число
#x из второй строки, которая выводит все позиции, на которых встречается число
#x в переданном списке.

lst = [int(i) for i in input().split()]
n = int(input())
if n not in lst:
    print('Отсутствует')
else:
    for i in range(len(lst)):
        if lst[i] == n:
            print(i, end=" ")