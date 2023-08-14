## 문제 : 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

import sys
N, M = map(int, sys.stdin.readline().split())  # 카드 개수, 합의 최대값
card = list(map(int, sys.stdin.readline().split()))
card.sort(reverse=True)

stop = False
suml = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = card[i]+card[j]+card[k]
            if sum > M:
                continue
            elif sum < M:
                suml.append(sum)
            else:
                stop = True
                print(sum)
                break
        if stop == True:
            break
    if stop == True:
        break
if stop == False:
    print(max(suml))


# 다른 분 코드 : i, j에서 반복을 N까지 할 필요가 없다.
import sys
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

mx = 0
for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      s = arr[i]+arr[j]+arr[k]
      if s<=M:
        if mx < s: mx = s
        break
print(mx)
