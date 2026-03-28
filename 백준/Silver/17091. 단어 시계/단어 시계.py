exp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "half"]
h = int(input())
m = int(input())
if m == 0:
    print(exp[h], "o' clock")
elif m <= 30:
    if m == 1:
        print(exp[m], "minute past", exp[h])
    elif m == 15 or m == 30:
        if m == 30:
            m = 21
        print(exp[m], "past", exp[h])
    elif m > 20:
        print(exp[20], exp[m % 10], "minutes past", exp[h])
    else:
        print(exp[m], "minutes past", exp[h])
else:
    if h == 12:
        h = 0
    m = 60 - m
    if m == 1:
        print(exp[m], "minute to", exp[h + 1])
    elif m == 15:
        print(exp[m], "to", exp[h + 1])
    elif m > 20:
        print(exp[20], exp[m % 10], "minutes to", exp[h + 1])
    else:
        print(exp[m], "minutes to", exp[h + 1])
