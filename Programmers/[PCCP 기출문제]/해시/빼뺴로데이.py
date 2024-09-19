## 문제 : 구매한 빼빼로를 오름차순으로 정렬하여 결과를 나타내 주세요.


def solution(pepero):
    answer = []
    pepero = set(pepero)
    pepero.sort()
    answer = pepero
    return answer

# 한줄로
def solution(pepero):
    return sorted(set(pepero))

