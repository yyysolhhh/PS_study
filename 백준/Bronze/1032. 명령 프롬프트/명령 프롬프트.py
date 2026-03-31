N = int(input())
file = []
for _ in range(N):
    file.append(list(input()))
for i in range(len(file)-1):
    for j in range(len(file[i])):
        if file[i][j] != file[i+1][j]:
            file[i+1][j] = '?'
print(''.join(file[-1]))