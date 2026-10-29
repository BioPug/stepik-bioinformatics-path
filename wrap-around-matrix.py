# Программа выводит таблицу размером n×n, заполненную числами от 1 до n**2
# по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке

n = int(input())
empty = [[0 for i in range(n)] for j in range(n)]
num = 1
row = 0
col = 0
step_col = 1
step_row = 0
for i in range(n**2):
    empty[row][col] = num
    num += 1
    next_row = row + step_row
    next_col = col + step_col
    if (0 <= next_col <n and 0 <= next_row < n) and empty[next_row][next_col] == 0:
        row = next_row
        col = next_col
    else:
        if step_row == 0 and step_col == 1:
            step_row = 1
            step_col = 0
        elif step_row == 1 and step_col == 0:
            step_row = 0
            step_col = -1
        elif step_row == 0 and step_col == -1:
            step_row = -1
            step_col = 0
        else:
            step_row = 0
            step_col = 1
        next_row = step_row + row
        next_col = step_col + col
        row = next_row
        col = next_col
for i in empty:
    print(*i)









