import sys
input = sys.stdin.readline

def pangram(sent):
    alpha = [0 for _ in range(26)]
    sent = sent.lower()
    for i in sent:
        if i.isalpha():
            alpha[ord(i) - ord('a')] += 1
    if min(alpha) == 0:
        return "Not a pangram"
    elif min(alpha) == 1:
        return "Pangram!"
    elif min(alpha) == 2:
        return "Double pangram!!"
    else:
        return "Triple pangram!!!"

n = int(input())
for i in range(1, n + 1):
    case = input().strip()
    ans = pangram(case)
    print(f"Case {i}: {ans}")