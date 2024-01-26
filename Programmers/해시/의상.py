## 문제 : 코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록


def solution(clothes):
    answer = 1
    hashdict = {i[1]: 0 for i in clothes}
    for i in clothes:
        hashdict[i[1]] += 1
    for i in hashdict.values():
        answer *= (i + 1)
    return answer - 1


# 위 풀이에서 hash를 만드는 부분을 짧게 할 수 있는 코드
def solution(clothes):
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
    answer = 1
    for type in hash_map:
        answer *= (hash_map[type] + 1)
    return answer - 1


# Counter로 푼 코드
from collections import Counter
from functools import reduce

def solution(clothes):
    counter = Counter([type for clothe, type in clothes])
    answer = reduce(lambda acc, cur: acc*(cur+1), counter.values(), 1) - 1
    return answer
