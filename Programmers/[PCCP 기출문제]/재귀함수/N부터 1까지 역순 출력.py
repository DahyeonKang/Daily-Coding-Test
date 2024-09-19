## 문제 : 입력된 N부터 1까지 역순으로 출력합니다.
# 우리는 재귀함수를 연습하는 부분으로
# for와 while같은 반복문을 사용하지 않습니다.


def num(N):
    if N == 0:
        return
    print(N)
    num(N-1)
n = int(input())
num(n)