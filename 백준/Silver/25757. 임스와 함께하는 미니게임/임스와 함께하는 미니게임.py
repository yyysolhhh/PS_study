import sys
input = sys.stdin.readline
num = {"Y": 1, "F": 2, "O": 3}
N, game = input().split()
players = [input() for _ in range(int(N))]
print(len(set(players)) // num[game])