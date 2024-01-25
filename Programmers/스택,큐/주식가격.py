## 문제 : 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.


def solution(prices):
    l = len(prices)
    answer = []

    for i in range(l - 1):
        time = 0
        price = prices[i]
        for j in range(i + 1, l):
            if price <= prices[j]:
                time += 1
            else:
                time += 1
                break
        answer.append(time)

    answer.append(0)
    return answer

# 유사한 풀이
def solution(prices):
    l = len(prices)
    answer = [0] * l

    for i in range(l - 1):
        for j in range(i + 1, l):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


# deque를 이용한 풀이
from collections import deque

def solution(prices):
    result = []  # 결과값
    queue = deque(prices)  # 주식가격 queue

    while queue:  # queue가 빈값이 아니면 while loop
        period = 0  # 가격이 떨어지지 않은 기간
        price = queue.popleft()  # i번째 주식 가격 추출

        for after in queue:  # 미래의 가격 목록
            period += 1  # 가격이 떨어지지 않은 기간 + 1초
            if price > after:  # 미래에 가격이 떨어졌다면
                break  # break
        result.append(period)  # 유지된 기간 결과값에 저장

    return result