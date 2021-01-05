def wages():
    import sys
    work_hours, rate, bonus = sys.argv[1:]
    work_hours = int(work_hours)
    rate = int(rate)
    bonus = int(bonus)
    result = work_hours*rate + bonus
    return result


salary = wages()
print(f'Зарплата сотрудника составит {salary} руб.')