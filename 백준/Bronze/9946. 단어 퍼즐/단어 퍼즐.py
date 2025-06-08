i = 1
while True:
    before = input()
    after = input()
    if before == "END" and after == "END":
        break
    if sorted(before) == sorted(after):
        ans = "same"
    else:
        ans = "different"
    print(f"Case {i}: {ans}")
    i += 1