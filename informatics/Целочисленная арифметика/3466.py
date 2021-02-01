import math
a = int(input())
b = int(input())
l = int(input())
N = int(input())

c = math.sqrt(a ** 2 + b ** 2)
L =  N*(N - 2) * c + a + 2 * l

print(round(L))