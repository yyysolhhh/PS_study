S = input()
if "A" in S:
    S = S.replace("B", "A").replace("C", "A").replace("D", "A").replace("F", "A")
elif "B" in S:
    S = S.replace("C", "B").replace("D", "B").replace("F", "B")
elif "C" in S:
    S = S.replace("D", "C").replace("F", "C")
else:
    S = len(S) * "A"
print(S)