## 문제 : 각 테스트 케이스에 대해 오타를 지운 문자열을 출력한다.

import sys
T = int(input())
for _ in range(T):
    i, str = sys.stdin.readline().split()
    s = list(str)
    s.pop(int(i) - 1)
    print(''.join(s))


# 다른 분 코드
T = int(input())

for i in range(T):
    n, word = input().split()
    n = int(n)
    print(word[:n-1], word[n:], sep='')