import sys, heapq
input = sys.stdin.readline
N = int(input())
timetable = [list(map(int, input().split())) for _ in range(N)]
timetable.sort()
room = []
heapq.heappush(room, timetable[0][1])
for i in range(1, N):
    if room[0] <= timetable[i][0]:
        heapq.heappop(room)
    heapq.heappush(room, timetable[i][1])
print(len(room))