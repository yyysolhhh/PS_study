n = int(input())
a = list(map(int, input().split()))
score = sum([1 if i % 2 == 1 else -1 for i in a])
print("Sad" if score >= 0 else "Happy")