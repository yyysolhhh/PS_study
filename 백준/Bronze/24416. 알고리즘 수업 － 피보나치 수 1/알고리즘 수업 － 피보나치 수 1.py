def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    f = [0 for _ in range(n + 1)]
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n), n - 2)