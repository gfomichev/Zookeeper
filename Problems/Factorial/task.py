N = int(input().strip())
result = 1

while N > 0:
    result *= N
    N -= 1

print(result)
