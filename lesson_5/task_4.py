eng_numerals = open(r"C:\Users\Arkady\Documents\ARCHPOD\PROGRAMMING\PYTHON\numerals.txt", encoding='utf-8')
rus_numerals = open(r"C:\Users\Arkady\Documents\ARCHPOD\PROGRAMMING\PYTHON\rus_numerals.txt", 'w', encoding='utf-8')

ru = ['один', 'два', 'три', 'четыре']

eng_list = [line.split() for line in eng_numerals]

i = 0
for l, j, k in eng_list:
    l = ru[i]
    i += 1
    ru_str = ' '.join([l, j, k])
    rus_numerals.write(ru_str + '\n')
    print(ru_str)

eng_numerals.close()
rus_numerals.close()
