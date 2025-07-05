import sys
N = int(input())
while True:
    print("? 1")
    sys.stdout.flush()
    s = input()
    if s == "Y":
        print(f"! 1")
        sys.stdout.flush()
        break