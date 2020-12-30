def int_func(text):
    return text.title()


print(int_func(input('Enter a word: ')))

#task 7
res_int_func = int_func(input('Enter some words - no initial capital: '))
print(res_int_func)