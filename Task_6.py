import re

short_plan = {}
with open('Task_6.txt', "r", encoding='utf-8') as long_plan:
    for line in long_plan:
        line_sp = line.split()
        disc = line_sp[0]
        nums = re.findall(r'\d*\.\d+|\d+', line)
        all_hours = sum(map(int, nums))
        short_plan.update({disc: all_hours})
    print(short_plan)


