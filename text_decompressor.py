# Программа восстанавливает текст из сжатой строки
# и сохраняет в файл.

d = {}
val = ''
ch = ''
path = "dataset_3363_2.txt"
with open(path, "r", encoding='utf-8') as f:
    for line in f:
        for i in line:
            if i.isalpha():
                if ch:
                    d[ch]=int(val)
                ch = i
                val = ''
            elif i.isdigit():
                val += str(i)
if ch:
    d[ch]=int(val)
result = ''.join(ch * val for ch, val in d.items())
with open('output.txt', "w", encoding='utf-8') as f:
    f.write(result)

