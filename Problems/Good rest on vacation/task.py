# put your python code here
duration, food_cost = [int(input()), int(input())]
flight_cost, hotel_cost = [int(input()), int(input())]
print(flight_cost * 2 + duration * food_cost + (duration - 1) * hotel_cost)
