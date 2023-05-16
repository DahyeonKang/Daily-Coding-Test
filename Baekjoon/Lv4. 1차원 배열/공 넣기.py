## 문제 : 을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.

import sys
N, M = map(int, sys.stdin.readline().split())
l = [0] * N
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    l[i-1:j] = [k] * (j - i + 1)
print(*l)
