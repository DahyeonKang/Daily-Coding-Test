## 문제 : 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.


def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)-1,-1,-1):
        answer.append(int(n[i]))
    return answer

print(solution(12345))


# 숫자 계산
def solution(n):
    answer = []
    while n > 10:
        answer.append(n%10)
        n // 10
    return answer


# 문자로 변경해서 뒤집기
def solution(n):
    n = str(n)
    n = list(n)
    n = n[::-1]
    answer = list(map(int, n))
    return answer
# 위 코드 한줄로
def solution(n):
    return list(map(int, str(n)))[::-1]