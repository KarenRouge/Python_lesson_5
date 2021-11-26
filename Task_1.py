user_str = input(f"Введите информацию: ")
new_file = open("My_file.txt", "w")
while True:
    user_str = input()
    new_file.write(user_str + '\n')
    if user_str == ' ':
        break
new_file.close
print("Запись данных завершена.")