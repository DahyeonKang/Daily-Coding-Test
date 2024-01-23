#@ 문제 :  각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.


# 샘플 테스트만 통화한 코드
import math
def solution(progresses, speeds):
    days = [-1]
    answer = []
    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)
        if days.pop() >= day:
            answer[-1] += 1
        else:
            answer.append(1)
            days.append(day)
    return answer


# 위 코드 수정한 버전 - 성공
import math
def solution(progresses, speeds):
    before_day = 0
    answer = []
    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)
        if before_day >= day:
            answer[-1] += 1
        else:
            answer.append(1)
            before_day = day
    return answer


# 비슷한 다른 사람 코드
import math

def solution(progresses, speeds):
    answer = []
    progress_day = [math.ceil((100 - x) / y) for x, y in zip(progresses, speeds)]
    print(progress_day)
    count = 0
    for i in progress_day:
        if i > count:
            answer.append(1)
            count = i
        else:
            answer[-1] += 1
    return answer

# 올림 기능을 음수 나누기로 구현한 코드
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]