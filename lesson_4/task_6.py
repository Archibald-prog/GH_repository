from itertools import count, cycle
for i in count(3):
    print(i)
    if i == 8:
        break

my_list = [2, 8, 7, 19, 5, 4, 0, 9]
score = 0
for i in cycle(my_list):
    print(i)
    score += 1
    if score == 8:
        break