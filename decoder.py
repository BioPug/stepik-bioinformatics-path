# Программа шифрует и расшифровывает текст по заданному ключу.
# Входные данные:
#   строка 1 — исходный алфавит,
#   строка 2 — конечный алфавит (i-й символ первой строки заменяется на i-й символ второй),
#   строка 3 — сообщение, которое нужно зашифровать,
#   строка 4 — сообщение, которое нужно расшифровать.
# Выходные данные: зашифрованная строка и расшифрованная строка, каждая на своей строке.

alphabet1 = input()
alphabet2 = input()
text_to_encrypt = input()
text_to_decrypt = input()

for i in text_to_encrypt:
    i = alphabet1.find(i)
    print(alphabet2[i],end='')
print()
for i in text_to_decrypt:
    i = alphabet2.find(i)
    print(alphabet1[i],end='')
