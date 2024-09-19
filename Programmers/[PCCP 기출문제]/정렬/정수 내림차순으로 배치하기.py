## 문제 : n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 

def solution(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))
