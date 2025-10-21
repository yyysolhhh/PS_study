import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(cur, dist):
    for nxt, nxt_d in graph[cur]:
        if visited[nxt] != -1:
            continue
        visited[nxt] = dist + nxt_d
        dfs(nxt, visited[nxt])

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, d = map(int, input().split())
    graph[p].append((c, d))
    graph[c].append((p, d))
visited = [-1 for _ in range(n + 1)]
visited[1] = 0
dfs(1, 0)
max_node, tmp = 0, 0
for i in range(1, n + 1):
    if visited[i] > tmp:
        tmp = visited[i]
        max_node = i
visited = [-1 for _ in range(n + 1)]
visited[max_node] = 0
dfs(max_node, 0)
print(max(visited))