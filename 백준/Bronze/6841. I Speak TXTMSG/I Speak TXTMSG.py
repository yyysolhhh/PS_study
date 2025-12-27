import sys
input = sys.stdin.readline
trans = {"CU": "see you", ":-)": "I’m happy", ":-(": "I’m unhappy", ";-)": "wink", ":-P": "stick out my tongue", "(~.~)": "sleepy", "TA": "totally awesome", "CCC": "Canadian Computing Competition", "CUZ": "because", "TY": "thank-you", "YW": "you're welcome", "TTYL": "talk to you later"}
while True:
    text = input().strip()
    if text in trans:
        print(trans[text])
    else:
        print(text)
    if text == "TTYL":
        break