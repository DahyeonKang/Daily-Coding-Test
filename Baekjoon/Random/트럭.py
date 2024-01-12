## 문제 : 출력은 표준출력을 사용한다. 모든 트럭들이 다리를 건너는 최단시간을 출력하라.

import sys
n, w, l =  map(int, sys.stdin.readline().split())  # 다리 건너는 트럭 수, 다리 길이, 다리 최대하중
truck = list(map(int, sys.stdin.readline().split()))
bridge = [0] * w
time = 0

while bridge:  # 다리에 트럭이 없으면 종료
    time += 1
    bridge.pop(0)
    if truck:
        if sum(bridge) + truck[0] <= l:
            bridge.append(truck.pop(0))
        else:
            bridge.append(0)
print(time)


