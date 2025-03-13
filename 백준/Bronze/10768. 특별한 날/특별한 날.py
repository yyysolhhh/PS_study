mon = int(input())
day = int(input())
if mon < 2:
    print("Before")
elif mon == 2 and day < 18:
    print("Before")
elif mon == 2 and day == 18:
    print("Special")
else:
    print("After")