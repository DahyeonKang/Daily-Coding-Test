## 문제 : 투표자 N명이 주어질 때 나올 수 있는 모든 경우의 수를 출력하는 프로그램을 작성해주세요.


def f(cnt, str):
    if cnt == 0:
        print(str)
        return
    f(cnt - 1, str + "O")
    f(cnt - 1, str + "X")

n = int(input())
f(n, "")


# 두번째 방법
def f(cnt, st):
    if cnt == 0:
        print(st)
        return
    oxox = "OX"
    for i in range(len(oxox)):
        f(cnt - 1, st + oxox[i])

n = int(input())
f(n, "")