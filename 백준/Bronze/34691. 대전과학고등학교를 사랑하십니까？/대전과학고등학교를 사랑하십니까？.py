import sys
input = sys.stdin.readline
hak = {"animal": "Panthera tigris", "tree": "Pinus densiflora", "flower": "Forsythia koreana"}
while True:
    w = input().strip()
    if w == "end":
        break
    print(hak[w])