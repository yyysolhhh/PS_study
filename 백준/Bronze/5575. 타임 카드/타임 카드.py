for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    start = sh * 60 * 60 + sm * 60 + ss
    end = eh * 60 * 60 + em * 60 + es
    t = end - start
    h = t // (60 * 60) % 24
    m = t // 60 % 60
    s = t % 60
    print(h, m, s)