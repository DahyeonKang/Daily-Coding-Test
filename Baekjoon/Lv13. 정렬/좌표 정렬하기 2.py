## 문제 : 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

import sys
n = int(sys.stdin.readline())
point = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
point.sort(key=lambda i: (i[1], i[0]))
for x, y in point:
    print(x, y)

# 다른 분 코드
import sys
cord = sys.stdin.readlines()[1:]
cord.sort(key=lambda x : (int(x.split()[1]), int(x.split()[0])))
print("".join(cord))