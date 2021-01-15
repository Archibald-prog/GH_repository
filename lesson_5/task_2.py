# the content of data.txt:
#
# this thing is not recommeded for eating 
# our town is too small 
# not very pleasant fact of life
# what does Marcellas Walles look like?


with open(r"C:\Users\Arkady\Documents\ARCHPOD\PROGRAMMING\PYTHON\data.txt") as file_1:
    i = 0
    for line in file_1:
        num = line.strip()
        i += 1
        print(f'Number of symbols in string {i} equals {len(num)}')
        print(f'Number of words in string {i} equals {len(num.split())}')
    print(f'Total number of strings equals {i}')
