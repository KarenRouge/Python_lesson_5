from   import next
rus_numbers = {1 : 'Один', 2 : 'Два', 3 : 'три', 4 : 'четыре'}
with open("Task_4.txt", "r") as eng_numbers:
    rus_list = {}
    eng_numbers_list = eng_numbers.read().split('\n')
    for str in eng_numbers_list:
        number = str.split()



