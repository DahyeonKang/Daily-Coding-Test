## 문제 : 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

# enumerate를 활용한 코드
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    print(queue)
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


# deque를 활용해서 location을 차례로 줄여가는 코드
from collections import deque
def solution(priorities, location):
    q = deque(priorities)
    answer = 0
    while q:
        m = max(q)
        l = q.popleft()
        location -= 1
        if l != m:
            q.append(l)
            if location < 0:
                location = len(q) - 1
        else:
            answer += 1
            if location < 0:
                break
    return answer


# 많은 분들이 성공한 코드

def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])
    print(d)
    while len(d):
        item = d.popleft()
        print(d, max(d)[0], item[0])
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


# 시도하려다 실패한 코드
def solution(priorities, location):
    answer = 0
    order = []
    # while priorities:
    #     idx = priorities.index(max(priorities))
    #     value = range(idx, len(priorities))
    #     order.extend(value)
    #     for _ in value:
    #         priorities.pop()
    # answer = order.index(location) + 1
    queue = [(i, p) for i, p in enumerate(priorities)]
    while False:  # priorities:
        m = max(priorities)
        max_l = [index + 1 for index, val in enumerate(priorities) if val == m]
        if len(max_l) == 1:
            value = range(idx, len(priorities))
            order.extend(value)
            for _ in value:
                priorities.pop()
        else:

    return answer
