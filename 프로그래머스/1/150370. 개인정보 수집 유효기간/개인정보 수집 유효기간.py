def expired_date(available, start):
    y, m, d = map(int, start.split("."))
    exp_m = m + available
    m = exp_m % 12
    y += exp_m // 12
    if m == 0:
        m = 12
        y -= 1
    print(y, m, d)
    return f"{y}.{m:02d}.{d:02d}"

def solution(today, terms, privacies):
    answer = []
    terms_dict = {i.split()[0]: int(i.split()[1]) for i in terms}
    for i, p in enumerate(privacies, start=1):
        date, term = p.split()
        if expired_date(terms_dict[term], date) <= today:
            answer.append(i)
    return answer