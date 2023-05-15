## 문제 : 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

import sys
list = []
while True:
    try:
        list.append(int(sys.stdin.readline()))
    except:
        break
max = max(list)
print(max)
print(list.index(max)+1)

# 다른 분 코드
a=[int(input()) for i in range(9)]
print(max(a))
print(a.index(max(a))+1)
