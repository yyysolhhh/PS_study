import sys
input = sys.stdin.readline
vowel = ["a", "e", "i", "o", "u"]

def rule1():
    for i in password:
        if i in vowel:
            return True
    return False

def rule2():
    for i in range(len(password) - 2):
        if password[i] in vowel and password[i + 1] in vowel and password[i + 2] in vowel:
            return False
        if password[i] not in vowel and password[i + 1] not in vowel and password[i + 2] not in vowel:
            return False
    return True

def rule3():
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            if password[i] in ["e", "o"]:
                continue
            return False
    return True

while True:
    password = input().strip()
    if password == "end":
        break
    if rule1() and rule2() and rule3():
        ans = "acceptable"
    else:
        ans = "not acceptable"
    print(f"<{password}> is {ans}.")