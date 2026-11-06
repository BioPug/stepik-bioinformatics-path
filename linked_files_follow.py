# Программа проходит по цепочке файлов: каждый файл (кроме последнего) содержит имя следующего.
# Останавливается, когда первое слово «We», и выводит содержимое последнего файла.

import requests
end = '699991.txt'
url = 'https://stepik.org/media/attachments/course67/3.6.3/'
while end != 'We':
    res = requests.get(url+end)
    text = res.text.strip()
    if text.split()[0] == 'We':
        print(text)
        break
    else:
        end = text.split()[0]

