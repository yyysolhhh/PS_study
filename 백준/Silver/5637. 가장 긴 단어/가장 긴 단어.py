import re

para = []
while True:
    try:
        para.extend(re.findall(r"[a-zA-Z-]+", input().strip()))
    except EOFError:
        break
ans = ""
l = 0
for w in para[:-1]:
    if l < len(w):
        ans = w
        l = len(w)
print(ans.lower())
