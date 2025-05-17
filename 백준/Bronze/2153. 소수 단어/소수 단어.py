def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

word = input()
total = 0
for w in word:
    if w.islower():
        total += ord(w) - ord("a") + 1
    else:
        total += ord(w) - 38
print("It is a prime word." if is_prime(total) else "It is not a prime word.")