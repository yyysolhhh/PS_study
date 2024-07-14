def num_of_case(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return num_of_case(n-1) + num_of_case(n-2) + num_of_case(n-3)
T = int(input())
for _ in range(T):
    n = int(input())
    print(num_of_case(n))
