N = int(input())
S = input()
if N <= 25:
    print(S)
else:
    if "." not in S[11:-12]:
        print(S[:11] + "..." + S[-11:])
    else:
        print(S[:9] + "......" + S[-10:])