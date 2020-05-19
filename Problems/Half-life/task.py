N = int(input().strip())
R = int(input().strip())
days = 0

while N >= R:
    days += 12
    N //= 2

print(days)
