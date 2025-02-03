N, M = map(int, input().split())
streak = dict()
for _ in range(N):
    line = input().split()
    *record, name = line
    max_streak = 0
    temp = 0
    for i in record:
        if i == ".":
            temp += 1
        elif i == "*":
            max_streak = max(max_streak, temp)
            temp = 0
        max_streak = max(max_streak, temp)
    streak[name] = max_streak
print(len(set(streak.values())))
for name, num in streak.items():
    print(num, name)