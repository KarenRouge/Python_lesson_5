rus_numbers = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
with open("Task_4.txt", "r+", encoding="utf-8") as eng_numbers:
    i = 1
    new_lines = []
    for line in eng_numbers:
        line_list = line.strip().split(' ')
        line_list.pop(0)
        line_list.insert(0, rus_numbers[i])
        new_line = ' '.join(line_list)
        print(new_line)
        new_lines.append(new_line)
        i = i + 1
        if i >= 5:
            break
    write_lines = "\n ".join(new_lines)
    print(write_lines)
    eng_numbers.writelines('\n' + write_lines)







