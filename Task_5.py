def func_1():
    try:
        with open('Task_5.txt', 'w+') as numbers:
            line = input('Введите цифры через пробел: ')
            numbers.writelines(line)
            num_spl = line.split()

            print(sum(map(int, num_spl)))
    except ValueError:
        print('Неправильно набраны числа. Введите целые числа через пробел')
func_1()
