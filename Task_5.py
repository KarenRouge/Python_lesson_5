line = (input("Введите числа через пробел: "))
with open("Task_5.txt", 'w+') as numbers:
    num = numbers.writelines(line)
    print(num)
    num_sp = num.split()
    print(sum(map(int, num_sp)))
