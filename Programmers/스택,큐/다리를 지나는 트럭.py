## 문제 : 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록


# 92점으로 하나가 시간 초과로 실패 -> for문 말고 while문으로 푸는 게 나을 것 같다.
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    B = deque([0] * bridge_length)

    for w in truck_weights:
        if sum(B) + w <= weight:  # 다리에 트럭이 올라갈 수 있는 경우
            answer += 1
            B.popleft()
            B.append(w)
        else:  # 무게 초과로 올라가지 못하는 경우
            while sum(B) + w > weight:
                answer += 1
                B.popleft()
                if sum(B) == 0:
                    B.append(w)
                    break
                else :
                    if sum(B) + w > weight:
                        B.append(0)
                    else:
                        B.append(w)
                        break
    if sum(B) != 0:
            return answer + bridge_length
    return answer



# 다른 분 코드에서 힌트 얻어, sum()을 지우고 변수에서 빼고 더하고를 반복함 - 성공
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    B = deque([0] * bridge_length)
    C = 0

    for w in truck_weights:
        if C + w <= weight:  # 다리에 트럭이 올라갈 수 있는 경우
            answer += 1
            C -= B.popleft()
            B.append(w)
            C += w
        else:  # 무게 초과로 올라가지 못하는 경우
            while C + w > weight:
                answer += 1
                C -= B.popleft()
                if C == 0:
                    B.append(w)
                    C += w
                    break
                else:
                    if C + w > weight:
                        B.append(0)
                    else:
                        B.append(w)
                        C += w
                        break
    if C != 0:
        return answer + bridge_length
    return answer



# while문 활용한 코드
from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    currentWeight = 0
    while len(truck_weights) != 0:
        time += 1

        currentWeight -= bridge.popleft()

        if currentWeight + truck_weights[0] <= weight:
            currentWeight += truck_weights[0]
            bridge.append(truck_weights.popleft())

        else:
            bridge.append(0)

    time += bridge_length

    return time