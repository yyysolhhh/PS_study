ans = 0
while True:
    try:
        gum_gum = input()
        ans += 1
    except EOFError:
        break
print(ans)