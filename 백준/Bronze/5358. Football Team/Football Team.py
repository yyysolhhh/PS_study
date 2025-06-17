while True:
    try:
        name = input()
        ans = ""
        for i in name:
            if i == "i":
                ans += "e"
            elif i == "e":
                ans += "i"
            elif i == "I":
                ans += "E"
            elif i == "E":
                ans += "I"
            else:
                ans += i
        print(ans)
    except EOFError:
        break