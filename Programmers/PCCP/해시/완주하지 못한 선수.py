## 문제 :

# 시간 초과
def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    return participant[0]


# 강사님 방법
def solution(participant, completion):
    part = {}
    # 명단별 참가자 인원
    for i in participant:
        if i in part:
            part[i] += 1
        else:
            part[i] = 1
    # 완주자 명단으로 참가자 인원 1명씩 감소,삭제
    for i in completion:
        if part[i] == 1:
            del part[i]
        else:
            part[i] -= 1

    answer = list(part)
    answer = answer[0]
    return answer

# 정렬 방법
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        # 중간에 다른게 있다면 그 참가자가 미완주자
        if participant[i] != completion[i]:
            return completion[i]
    # 모두다 같다면 마지막 참가자가 미완주자
    return participant[-1]





## 우선선위를 주는 정렬
# l3 = [[1,2], [5,3], [3,3], [7,4], [6,1]]
# print(l3)
#
# l3.sort(key = lambda x : (x[1], -x[0]) )
# print(l3)