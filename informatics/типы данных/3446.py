import math
def func():
    n = 10
    pi = 0
    for i in range(1, 10, 2):
        pi += 4/i - 4 / (i + 2)
    print(pi)