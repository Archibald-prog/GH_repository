import math


def fact(n):
    for el in range(1, n + 1):
        yield math.factorial(el)


n = int(input('Enter n: '))
fact_list = [el for el in fact(n)]
print(fact_list)
