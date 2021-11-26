rus_numbers = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
with open("Task_4.txt", "r") as eng_numbers:
    rus_numbers = []
    eng_numbers_list = eng_numbers.read().split('\n')
    for number in eng_numbers_list:
        number_sp = number.split(' вЂ” ')
        for key in rus_numbers:
            new_number = str(rus_numbers[key]) + ' - ' + number_sp[1]
            print(new_number)
            rus_numbers.append(new_number)
    print(rus_numbers)







