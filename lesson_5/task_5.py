from functools import reduce

with open(r"C:\Users\Arkady\Documents\ARCHPOD\PROGRAMMING\PYTHON\user_data.txt", 'w+') as user_file:

    numbers = ['10', '3', '15', '5', '1', '0']
    user_file.writelines("%s " % line for line in numbers)
    
    print(reduce(lambda x, y: float(x) + float(y), numbers))
    