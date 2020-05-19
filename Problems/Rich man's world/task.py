initial_sum = int(input().strip())
protected_sum = 700000
years = 0
rate = 1.071
while initial_sum < protected_sum:
    initial_sum *= rate
    years += 1
print(years)
