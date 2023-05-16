## 문제 : 공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.

import sys
N, M = map(int, sys.stdin.readline().split())
l = list(range(1, N+1))
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    temp = l[i-1]
    l[i-1] = l[j-1]
    l[j-1] = temp
print(*l)

# 다른 분 코드
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [i for i in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x], a[y] = a[y], a[x]
print(*a[1:])
