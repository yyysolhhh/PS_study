N = int(input())
liquids = list(map(int, input().split()))
st, en = 0, N - 1
ans_st, ans_en = liquids[st], liquids[en]
while st < en:
    if abs(ans_st + ans_en) > abs(liquids[st] + liquids[en]):
        ans_st = liquids[st]
        ans_en = liquids[en]
    if liquids[st] + liquids[en] < 0:
        st += 1
    else:
        en -= 1
print(ans_st, ans_en)
