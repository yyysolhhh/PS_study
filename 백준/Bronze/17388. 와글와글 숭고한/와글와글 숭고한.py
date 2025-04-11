univ = ["Soongsil", "Korea", "Hanyang"]
num = list(map(int, input().split()))
print("OK" if sum(num) >= 100 else univ[num.index(min(num))])