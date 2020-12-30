def my_func(x, y):
    try:
        result = x ** y
    except TypeError:
        return 'Введите вещественное число'
    return result


# решение с циклом
# def my_func(x, y):
#     num = x
#     for i in range(abs(y) - 1):
#         num = num*x
#         power = 1/num
#     return power

print(my_func(6, -3))
