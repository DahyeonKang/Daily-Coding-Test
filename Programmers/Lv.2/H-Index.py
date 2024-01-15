## 문제 : H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.


def solution(citations):
    answer = -1
    h = 0
    count = 0
    n = len(citations)
    citations.sort(reverse=True)
    while h == n-1:
        h += 1
        if h == citations[h-1]:
            answer = h
            return h
    return answer

print(solution([3, 0, 6, 1, 5]))