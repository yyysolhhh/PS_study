import sys
input = sys.stdin.readline

def func(n):
    if n < 2023:
        return 0
    
    target = '2023'
    cnt = 0
    
    for i in range(2023, n+1):
        idx = 0
        for j in str(i):
            if j == target[idx]:
                idx += 1
                if idx == 4:
                    cnt += 1
                    break
    return cnt
            
        
if __name__ == "__main__":
    n = int(input())
    print(func(n))