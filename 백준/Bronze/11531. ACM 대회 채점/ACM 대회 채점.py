probs = dict()
cnt = 0
time = 0
while True:
    log = input()
    if log == "-1":
        break
    m, prob, result = log.split()
    if result == "right":
         cnt += 1
         time += int(m)
         if prob in probs:
             time += probs[prob] * 20
    elif result == "wrong":
        if prob not in probs:
            probs[prob] = 1
        else:
            probs[prob] += 1
print(cnt, time)