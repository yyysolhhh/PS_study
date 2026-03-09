card_set = set(map(int, input().split()))
number_list = [i if i in card_set else 0 for i in range(9 + 1)]

minimum_count = 6

for i in range(1, 6):
    number_sequence = number_list[i:i + 5]
    count = number_sequence.count(0)

    if count < minimum_count:
        minimum_count = count

print(minimum_count)