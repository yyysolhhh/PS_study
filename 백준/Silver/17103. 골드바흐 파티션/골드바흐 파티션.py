import sys
input = sys.stdin.readline
def checkPrimeNum(n):
    primeNumList = [False, False] + [True] * n
    for i in range(2, int(n**0.5)+1):
        for j in range(i+i, n+1, i):
            if primeNumList[j]:
                primeNumList[j] = False
    return primeNumList
T = int(input())
N = [int(input()) for _ in range(T)]
primeNum = checkPrimeNum(max(N))
for i in N:
    goldbachPartition = 0
    for j in range(2, i//2+1):
        if primeNum[j] and primeNum[i-j]:
            goldbachPartition += 1
    print(goldbachPartition)