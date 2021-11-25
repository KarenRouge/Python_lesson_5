def split_list(income, size):
    name1 = []
    while len(income) > size:
        piece = income[:size]
        name1.append(piece)
        income = income[size:]
        name1.append(income)
        return name1


with open("Task_3.txt", "r") as income:
    name_1 = income.readlines()
    print(name_1)
    i = 1
    for name_1 in range(1, 4):
        name_1 = split_list(name_1, i)
        i = i + 1
