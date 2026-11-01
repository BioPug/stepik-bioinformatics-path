# Функция, которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два

lst = [int(i) for i in input().split()]
def modify_list(x):
    for i in range(len(x)-1,-1,-1):
        if x[i] % 2 != 0:
            del x[i]
        else:
            x[i] = x[i] //2
modify_list(lst)
print(lst)


