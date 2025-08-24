import sys

def solve():

    input = sys.stdin.readline

    n = int(input())
    hangers = list(map(int, input().split()))
    u, d = map(int, input().split())
    tops_only_hangers = hangers.count(1)
    bottoms_only_hangers = hangers.count(2)
    if u < tops_only_hangers or d < bottoms_only_hangers:
        print("NO")
        return
    print("YES")
    remaining_tops = u - tops_only_hangers
    
    result = []
    for hanger_type in hangers:
        if hanger_type == 1:
            result.append('U')
        elif hanger_type == 2:
            result.append('D')
        elif hanger_type == 3:
            if remaining_tops > 0:
                result.append('U')
                remaining_tops -= 1
            else:
                result.append('D')
    
    print("".join(result))

solve()