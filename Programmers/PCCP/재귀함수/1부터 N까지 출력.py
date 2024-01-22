## 문제 : 1부터 입력된 N까지 출력합니다.
# 우리는 재귀함수를 연습하는 부분으로
# for와 while같은 반복문을 사용하지 않습니다.


def num(N):
    if N == 0:
        return
    num(N - 1)
    print(N)


n = int(input())
num(n)

# 재귀함수에서 출력과 재귀함수부분을 바꾸면 순서가 뒤바뀐다.