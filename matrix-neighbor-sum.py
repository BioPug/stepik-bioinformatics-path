# Программа, на вход которой подаётся прямоугольная матрица
# в виде последовательности строк.
# После последней строки матрицы идёт строка, содержащая только строку "end"
# Программа выводит матрицу того же размера,
# у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы
# на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
# У крайних символов соседний элемент находится с противоположной стороны матрицы


x = []
while True:
    a = input()
    if a == 'end':
        break
    else:
        x.append([int(i) for i in a.split()])
row = len(x)
col = len(x[0])
res = [[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        up = (i - 1) % row
        down = (i + 1) % row
        left = (j - 1) % col
        right = (j + 1) % col
        res[i][j] = x[i][left]+x[i][right]+x[up][j]+x[down][j]
for i in res:
    print(' '.join(str(i) for i in i))


