with open(r"C:\Users\Arkady\Documents\ARCHPOD\PROGRAMMING\PYTHON\user_data.txt", 'w+') as user_file:

    while True:
        line = user_file.write(input('Enter a string or press Enter to stop: '))
        if not line:
            break
            