n = int(input())
word = input()
hid = []
for i in range(len(word)):
    if word[i].isdigit():
        if i > 0 and word[i - 1].isdigit():
            hid[-1] += word[i]
        else:
            hid.append(word[i])
print(sum(map(int, hid)))