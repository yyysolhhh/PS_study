N, K = input().split()
N = int(N)
K = int(K)
circle = [i for i in range(1, N+1)]
josephus = []
sequence = K - 1
while circle:
    if sequence >= len(circle):
        sequence = sequence % len(circle)
    else:
        josephus.append(str(circle.pop(sequence)))
        sequence += K - 1
print("<" + ", ".join(josephus) + ">")
