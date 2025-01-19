T = int(input())
for i in range(1, T + 1):
    B = int(input())
    case = input().replace("O", "0").replace("I", "1")
    ans = [chr(int(case[i:i + 8], 2)) for i in range(0, len(case), 8)]
    print(f"Case #{i}: {"".join(ans)}")