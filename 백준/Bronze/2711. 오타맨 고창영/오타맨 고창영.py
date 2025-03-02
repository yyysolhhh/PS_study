T = int(input())
for _ in range(T):
    loc, string = input().split()
    loc = int(loc) - 1
    string = string[:loc] + string[loc + 1:]
    print(string)