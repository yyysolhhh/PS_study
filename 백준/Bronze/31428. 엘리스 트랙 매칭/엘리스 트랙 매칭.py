cloud = {"C": 0, "S": 0, "I": 0, "A": 0}
N = int(input())
tracks = input().split()
for t in tracks:
    cloud[t] += 1
h = input()
print(cloud[h])