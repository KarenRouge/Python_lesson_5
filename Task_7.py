with open('Task_7.txt', 'r+') as firm_list:
    income_dict_firm = {}
    rub_dict_firm = {}
    for line in firm_list:
        parts = line.split()
        income = int(parts[2]) - int(parts[3])
        if income > 0:
            income_dict_firm.update({parts[1]: income})
        else:
            rub_dict_firm.update({parts[1]: income})
    income_dict = {"Average": str(sum(map(int, income_dict_firm.values())))}
    income_dict_firm.update(rub_dict_firm)
    income_dict_firm.update(income_dict)
    import json
    json.dump(income_dict_firm, firm_list)
