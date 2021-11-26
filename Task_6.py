
short_plan = {}
with open('Task_6.txt', "r") as long_plan:
    for line in long_plan:
        line1 = int(filter(line.isdigit, line))
        print(line1)
