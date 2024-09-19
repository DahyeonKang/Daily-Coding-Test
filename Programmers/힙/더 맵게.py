## 문제 :

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    m1 = heapq.heappop(scoville)
    if m1 >= K:
        return 0

    while True:
        try:
            answer += 1
            m2 = heapq.heappop(scoville)
            heapq.heappush(scoville, m1 + (m2 * 2))
            m1 = heapq.heappop(scoville)
            if m1 >= K:
                return answer
        except:
            return -1


#
import heapq as hq
def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer



# 연결이 일직선으로만 된 상태일 떄만 적용 가능한 코드
def solution(n, wires):
    answer = n
    for i in range(1, n - 2):
        print(i)
        diff = abs(len(set(sum(wires[:i], []))) - len(set(sum(wires[i + 1:], []))))
        if answer > diff:
            answer = diff
    return answer