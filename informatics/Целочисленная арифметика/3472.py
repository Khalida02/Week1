n = int(input())

res = n * 45
for i in range(1, 11):
    if i % 2 == 1:
        res += 5
    else:
        res += 15

hour = (540 + res)//60
minute = (540 + res)%60
print(hour, minute)