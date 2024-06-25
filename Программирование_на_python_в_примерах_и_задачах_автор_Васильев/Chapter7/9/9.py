name = "test1"
use_name = f"/Users/dmitrijiakovlev/Desktop/Program/pycharm/Chapter7/9/{name}.txt"
first_f = open(use_name)
txt1 = first_f.read()
print("Исходный файл прочитан:\n", txt1, sep="")
first_f.close()
try:
    print("Копия файла:")
    use_name = f"/Users/dmitrijiakovlev/Desktop/Program/pycharm/Chapter7/9/{name}.txt"
    first_f = open(use_name)
    second_f = open("/Users/dmitrijiakovlev/Desktop/Program/pycharm/Chapter7/9/copy_test1.txt", "xt")
    k = 1
    for l in first_f:
        second_f.write(str(k)+") "+l)
        k += 1
    first_f.close()
    second_f.close()
    second_f = open("/Users/dmitrijiakovlev/Desktop/Program/pycharm/Chapter7/9/copy_test1.txt")
    txt2 = second_f.read()
    print(txt2)
except FileExistsError:
    print("Ошибка: такой файл уже существует")
except:
    print("Ошибка доступа к файлу")
