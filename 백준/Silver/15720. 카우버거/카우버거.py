B, C, D = map(int, input().split())
burgers = sorted(map(int, input().split()), reverse=True)
sides = sorted(map(int, input().split()), reverse=True)
drinks = sorted(map(int, input().split()), reverse=True)
set_cnt = min(B, C, D)
set_price = 0
for i in range(set_cnt):
    set_price += burgers[i] + sides[i] + drinks[i]
discount = int(set_price * 0.9)
others = sum(burgers[set_cnt:]) + sum(sides[set_cnt:]) + sum(drinks[set_cnt:])
print(set_price + others)
print(discount + others)