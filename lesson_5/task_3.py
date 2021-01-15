# the content of wages.txt:
# Ivanov 21500.12
# Petrov 19000.08
# Sidorov 43000.50
# Shapkin 15000.30
# Bulkin 10500.10
# Gavrilov 8300.03
# Kuznetsov 7600.99
# Yakovlev 41000.34
# Skobin 20500.01
# Krasnov 21200.87
#

def average(numbers):
    return float(sum(numbers) / len(numbers))


with open(r"C:\Users\Arkady\Documents\ARCHPOD\PROGRAMMING\PYTHON\wages.txt") as wages:

    whole_staff_list = [line.split() for line in wages]
    wages_list = [float(val) for i, val in whole_staff_list]
    print('Employees with wages less than 20.000: ')
    min_wages_list = [print(i, float(val)) for i, val in whole_staff_list if float(val) < 20000]
    print(f'The average pay of employees on the staff equals {average(wages_list):.2f} ')
