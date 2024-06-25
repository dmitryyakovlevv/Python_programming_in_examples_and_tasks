name = "test1"
text = "qwerty"
try:
    use_name = f"/Users/dmitrijiakovlev/Desktop/Program/pycharm/Chapter7/10/{name}.txt"
    first_f = open(use_name, "xt")
    first_f.write(text.upper())
    first_f.close()
    first_f = open(use_name)
    print("Файл создан, содержимое файла:\n", first_f.read(), sep="")
except FileExistsError:
    print("Ошибка: такой файл уже существует")
except:
    print("Ошибка доступа к файлу")