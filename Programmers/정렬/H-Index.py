## 문제 : H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.


# 성공 2
def solution(citations):
    n = len(citations)
    for h in range(max(citations), -1, -1):
        higher = sum([1 if i >= h else 0 for i in citations])
        if higher >= h and (n-higher) <= h:
            return h


# 다른 분 코드
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0