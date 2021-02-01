x = int(input())

next = "The next number for the number {} is {}."
prev = "The previous number for the number {} is {}."

print(next.format(x, x + 1))
print(prev.format(x, x - 1))