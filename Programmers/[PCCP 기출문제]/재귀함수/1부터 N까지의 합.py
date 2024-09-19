## 문제 : 꼬리재귀함수 - 1부터 입력된 N까지의 합을 출력합니다.


def num(N):
    if N == 1:
        return 1
    return N + num(N-1)

n = int(input())
print(num(n))