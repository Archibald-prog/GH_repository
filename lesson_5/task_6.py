import re
from functools import reduce

with open(r"C:\Users\Arkady\Documents\ARCHPOD\PROGRAMMING\PYTHON\dictionary.txt", encoding='utf-8') as my_classes:
    res_dict = {}
    for line in my_classes:
        keys = line.split(':')[0]
        values = re.findall('\d+', line)
        int_values = [int(item) for item in values]
        for val in int_values:
            res_dict[keys] = reduce(lambda x, y: x + y, int_values)
    print(res_dict)
