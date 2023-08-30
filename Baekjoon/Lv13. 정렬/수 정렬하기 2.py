## 문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys
N = int(sys.stdin.readline())
# l = []
l = [int(sys.stdin.readline().strip()) for _ in range(N)]
print(sorted(l), sep='\n')
# for _ in range(N):
#     l.append(int(sys.stdin.readline()))
