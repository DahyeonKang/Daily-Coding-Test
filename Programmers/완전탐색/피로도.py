## 문제 : 유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때,
# 유저가 탐험할수 있는 최대 던전 수를 return


from itertools import permutations
def solution(k, dungeons):
    answer = -1

    for p in permutations(dungeons, len(dungeons)):
        temp = k
        count = 0
        for min, minus in p:
            if temp >= min:
                count += 1
                temp -= minus
            else:
                break
        if count > answer:
            answer = count
    return answer


# 마지막 크기 비교 부분 짧게 하기
from itertools import permutations
def solution(k, dungeons):
    answer = -1

    for p in permutations(dungeons, len(dungeons)):
        temp = k
        count = 0
        for min, minus in p:
            if temp >= min:
                count += 1
                temp -= minus
            else:
                break
        answer = max(count, answer)
    return answer


# 정렬을 활용한 코드 - 18, 19번 테스트케이스 실패 
def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0],x[1]))
    for x,y in dungeons:
        print("x :", x, "y : ", y)
        if k >= x:
            k -= y
            answer += 1
    return answer