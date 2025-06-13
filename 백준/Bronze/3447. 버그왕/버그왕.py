while True:
    try:
        line = input()
        while "BUG" in line:
            line = line.replace("BUG", "")
        print(line)
    except EOFError:
        break