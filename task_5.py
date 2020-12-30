def summary():
    ex = False
    result = 0
    while ex == False:
        numbers = input('Enter numbers or q to exit: ').split()
        res_line = 0
        for num in numbers:
            if 'q' in num:
                ex = True
                break
            res_line += int(num)
        result += res_line
    return result