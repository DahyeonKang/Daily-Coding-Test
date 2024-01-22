## 문제 : 다원이를 도와서 다원이의 바둑판에 바둑돌이 몇개나 필요한지 계산하는 프로그램을 작성해주세요.


# def f(low, col):
#     if low % 2 == 0 and col % 2 == 0:
#         return 0
#     return 1 + 4 * f(low//2, col//2)
# n, m = map(int, input().split())
# print(f(n, m))

def f(low, col):
    # 끝나는 조건
    if low % 2 == 0 or col % 2 == 0:
        return 0

    # 일딴 가능
    return 1 + 4 * f(low//2, col//2)

# 만약 가능하다면 1개를 추가
# 추가 하고나서 남은 공간이 홀수라면 4개를 추가
# 남는 공간이 짝수가 있다면 0개를 추가
n, m = map(int, input().split())

print(f(n, m))