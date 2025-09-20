sounds = {"A": 0, "A#": 1, "Bb": 1, "B": 2, "Cb": 2, "B#": 3, "C": 3, "C#": 4, "Db": 4, "D": 5, "D#": 6, "Eb": 6, "E": 7, "Fb": 7, "E#": 8, "F": 8, "F#": 9, "Gb": 9, "G": 10, "G#": 11, "Ab": 11}
rev_sounds = {0: "A", 1: "A#", 2: "B", 3: "C", 4: "C#", 5: "D", 6: "D#", 7: "E", 8: "F", 9: "F#", 10: "G", 11: "G#"}
while True:
    eum = input().split()
    if eum[0] == "***":
        break
    num = int(input())
    for i in eum:
        idx = sounds[i] + num
        if idx < 0:
            idx += 12
        print(rev_sounds[idx % 12], end=" ")
    print()