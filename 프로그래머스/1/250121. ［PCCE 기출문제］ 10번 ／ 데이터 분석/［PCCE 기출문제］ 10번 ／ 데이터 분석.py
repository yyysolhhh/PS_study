def basis(s):
    if s == "code":
       	return 0
    elif s == "date":
        return 1
    elif s == "maximum":
        return 2
    elif s == "remain":
        return 3
        
def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_i = basis(ext)
    sort_i = basis(sort_by)
    for d in data:
        if d[ext_i] < val_ext:
            answer.append(d)
    answer.sort(key=lambda x: x[sort_i])
    return answer