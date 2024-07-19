def is_prime(n):
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    else:
        return True
num = [i for i in range(1, 123456 * 2 + 1)]
prime = []
for i in num:
    prime.append(is_prime(i))
while True:
    n = int(input())
    if n == 0:
        break
    print(prime[n:2*n].count(True))