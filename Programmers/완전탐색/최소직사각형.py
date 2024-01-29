## 문제 : 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다.
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return

def solution(sizes):
    long = []
    short = []
    for w, h in sizes:
        long.append(max(w, h))
        short.append(min(w, h))
    answer = max(long) * max(short)
    return answer


# 더 짧은 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)