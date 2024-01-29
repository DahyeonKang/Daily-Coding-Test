## 문제 : 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return


# 참고 : Set 자료형은 Noniterable이라서 인덱싱이 안되고, for문에서 돌 수는 있음

from itertools import permutations
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    P = []
    for i in range(1, len(numbers) + 1):
        P.extend([int(''.join(list(i))) for i in list(permutations(numbers, i))])

    for num in set(P):
        count = 0
        for i in range(2, num):
            count += 1
            if num % i == 0:
                break
        if count == (num - 2):
            answer += 1

    return answer



# 짧은 코드 - set 특징 살린 코드
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
        # 순열의 각 결과에서 문자열로 -> 정수형으로 변환, |= : union한다는 의미
    a -= set(range(0, 2))
    # 0, 1 제거
    for i in range(2, int(max(a) ** 0.5) + 1):
    # 약수가 대칭적으로 나오기 때문에 sqrt(n)까지 봐도 된다.
        a -= set(range(i * 2, max(a) + 1, i))
        # 에라토스테네스의 체 구현 
    return len(a)
