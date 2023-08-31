## 문제 : 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

import sys
n = list(sys.stdin.readline().strip())
n.sort(reverse=True)  # n.sort(reverse=1)로도 가능
print("".join(n))  # sep으로 대체 가능

# 다른 분 코드 : 짧게 잘 작성하셨다.
print(*sorted(sys.stdin.readline(), reverse=True), sep="")

# 다른 분 코드 : ""
print(''.join(sorted([*input()], reverse=1)))