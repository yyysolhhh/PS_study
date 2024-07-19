from itertools import permutations
import sys
input = sys.stdin.readline
def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(list(map(int, input().split())))
    paths = permutations(range(N))
    cost = sys.maxsize
    for p in paths:
        if W[p[-1]][p[0]] == 0:
            continue
        temp = 0
        check = True
        for i in range(N-1):
            start = p[i]
            end = p[i+1]
            if W[start][end] == 0:
                check = False
                break
            temp += W[start][end]
            if temp >= cost:
                check = False
                break
        if check == False:
            continue
        temp += W[p[-1]][p[0]]
        cost = min(cost, temp)
    return cost
print(main())