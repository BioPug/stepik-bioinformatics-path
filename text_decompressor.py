# Программа восстанавливает текст из сжатой строки
# и сохраняет в файл.

result = ''
val = ''
ch = ''
path = "dataset_3363_2.txt"
with open(path, "r", encoding='utf-8') as f:
    for line in f:
        for i in line:
            if i.isalpha():
                if ch:
                    result += ch * int(val)
                ch = i
                val = ''
            elif i.isdigit():
                val += str(i)
if ch:
    result += ch * int(val)
with open('output.txt', "w", encoding='utf-8') as f:
    f.write(result)

