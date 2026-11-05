# Программа скачивает файл по ссылке, считает число строк.

import requests
url = ''
res = requests.get(url).text
line_count = len(res.splitlines())
print(line_count)
