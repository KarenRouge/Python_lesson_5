with open("Task_3.txt", "r") as income:
    less20 = []
    salary_each = []

    income_each = income.read().split('\n')
    for each in income_each:
        each = each.split()
        salary_each.append(each[1])
    for each in income_each:

        each = each.split()
        if int(each[1]) < 20000:
            less20.append(each[0])
    print(salary_each)
    print(f"Оклад меньше 20.000 имеют: {less20}. {sum(map(int, salary_each)) / len(salary_each)}")
