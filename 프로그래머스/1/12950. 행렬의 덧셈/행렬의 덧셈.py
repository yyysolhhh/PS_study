def solution(arr1, arr2):
    result = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return result