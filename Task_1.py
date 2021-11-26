user_str = input(f"Введите информацию: ")

with open("My_file.txt", "x") as new_file:
    while True:
        user_str = input()
        new_file.write(user_str + '\n')
        if user_str == ' ':
            break

print("Запись данных завершена.")