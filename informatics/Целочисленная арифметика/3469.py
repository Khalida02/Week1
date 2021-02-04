n = int(input())
n = n % (24 * 3600)
hour = n // 3600

n = n % 3600
minute = n // 60
seconds = n % 60
print(hour, ":", minute, ":", seconds) 