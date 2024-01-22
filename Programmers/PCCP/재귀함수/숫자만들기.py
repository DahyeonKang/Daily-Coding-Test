## 문제 : N보다 작거나 같은 자연수 중 Q의 원소로만 구성된 가장 큰 수를 출력해주세요.


def f(sum, maxnum):
    # 끝나는 조건
    if N < sum:
        return maxnum

    # 끝나지 않으면 가장 큰 수는?
    maxnum = max(sum, maxnum)

    # 재귀함수가 호출되는 규칙
    for i in range(K):
        maxnum = f(sum * 10 + Q[i], maxnum)

    return maxnum


N, K = map(int, input().split())
Q = list(map(int, input().split()))
print(f(0, 0))  # 마지막 자리가 계산해서 가지고 다니는 값