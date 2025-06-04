N = int(input())
mascot = input()
K = int(input())
if mascot == "annyong":
    if K % 2 == 1:
        print(K)
    else:
        print(K - 1)
elif mascot == "induck":
    if K % 2 == 0:
        print(K)
    else:
        print(K + 1 if K < N else K - 1)