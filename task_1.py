def division(num_1, num_2):
    try:
        answer = num_1 / num_2
    except ZeroDivisionError:
        return 'Деление на ноль!'
    except ValueError:
        return 'Ошибка. Введите число!'
    return answer


print(division(float(input('Введите делимое: ')), float(input('Введите делитель: '))))
