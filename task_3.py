def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    result = sum(my_list) - min(my_list)
    return result


try:
    print(my_func(float(input('Введите первое число: ')), float(input('Введите второе число: ')),
    float(input('Введите третье число: '))))
except ValueError:
    print('Ошибка! Введите число.')