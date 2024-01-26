## 문제 : 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.


# 케이스를 통과했지만 효율성 검사 실패
def solution(participant, completion):
    answer = ''
    for name in completion:
        participant.remove(name)
    answer = participant[0]
    return answer



# 효율성을 만족시킬 수 있는 코드들
## 1) sort() 정렬 이용
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i, j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1]


## 2) hash) 알고리즘 이용
def solution(participant, completion):
    hash_dict = {}
    sumHash = 0

    for i in participant:
        hash_dict[hash(i)] = i
        sumHash += hash(i)

    for j in completion:
        sumHash -= hash(j)

    return hash_dict[sumHash]


## 3) Counter 라이브러리 사용
from collections import Counter

def solution(participant, completion):
    answer = ''
    dict_result=Counter(participant)-Counter(completion)
    return list(dict_result.keys())[0]