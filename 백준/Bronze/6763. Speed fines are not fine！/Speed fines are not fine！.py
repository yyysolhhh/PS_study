limit = int(input())
speed = int(input())
if limit >= speed:
    print("Congratulations, you are within the speed limit!")
else:
    if 1 <= speed - limit <= 20:
        fine = 100
    elif 21 <= speed - limit <= 30:
        fine = 270
    else:
        fine = 500
    print(f"You are speeding and your fine is ${fine}.")