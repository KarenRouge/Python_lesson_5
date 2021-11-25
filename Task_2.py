str_list = ["apple 45", "Orange 345", "Banana 22 22"]
with open("Task_2.txt", "w+") as my_file:
    for el in str_list:
        my_file.write(el)
        my_file.write("\n")
    my_file.seek(0)
    str_count = my_file.readlines()
    print(f"Количество строк в файле: {len(str_count)}")
    my_file.seek(0)
    i = 0
    for el in str_list:
        words = len(el.split(' '))
        i = i + 1
        print(f"Количество слов в {i} строке: {words}")
