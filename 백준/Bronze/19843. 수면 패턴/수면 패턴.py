day = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5}
T, N = map(int, input().split())
sleep = 0
for _ in range(N):
    D1, H1, D2, H2 = input().split()
    H1, H2 = int(H1), int(H2)
    diff = day[D2] - day[D1]
    if diff == 0:
        sleep += H2 - H1
    elif diff > 0:
        sleep += 24 * diff - H1 + H2
need = T - sleep
if need < 0:
    print(0)
elif need > 48:
    print(-1)
else:
    print(need)
