l = int(input())
s = input()
cnt_e = s.count("e")
cnt_2 = s.count("2")
if cnt_e > cnt_2:
    print("e")
elif cnt_e < cnt_2:
    print("2")
else:
    print("yee")