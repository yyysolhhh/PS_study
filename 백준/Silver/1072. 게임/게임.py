import math
X, Y = map(int, input().split())
Z = math.floor(100 * Y / X)
MAX = 1000000000
start, end = 1, MAX
cnt = 0
if Z >= 99:
    print(-1)
else:
   while start <= end:
       mid = (start + end) // 2
       temp_z = math.floor(100 * (Y + mid) / (X + mid))
       if temp_z <= Z:
           start = mid + 1
       else:
           end = mid - 1
           cnt = mid
   print(cnt)
