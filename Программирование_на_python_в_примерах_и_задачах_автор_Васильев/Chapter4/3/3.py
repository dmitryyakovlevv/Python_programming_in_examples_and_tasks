s = "абвгдеёжзиклмнопрстуфхцшщчйьъяaaaaaaa"
m = {'а', 'е', 'ё', 'и', 'о', 'у', 'я'}
for i in s:
    if i in m:
        print(i, end=" ")