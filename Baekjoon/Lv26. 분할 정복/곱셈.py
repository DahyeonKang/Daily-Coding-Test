## 문제 : 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

# 시간 초과
a, b, c = map(int, input().split())
print((a**b)%c)

# 성공
def solution(a, b, c):
    if b == 1:
        return a % c
    temp = solution(a, b // 2, c)
    if b % 2 == 1:
        return ((temp * temp) % c) * a % c
    else:
        return (temp * temp) % c
a, b, c = map(int, input().split())
print(solution(a, b, c))