t = int(input())
for i in range(1, t + 1):
    n, m = map(int, input().split())
    ans = (m - n + 1) * (n + m) // 2
    print(f"Scenario #{i}:\n{ans}\n")