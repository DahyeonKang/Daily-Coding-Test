## 문제 : 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사하기

from functools import reduce
X = int(input())
N = int(input())
sum = 0
for i in range(N):
    sum += reduce(lambda x,y : x*y, map(int, input().split()))  # 가격, 개수
if sum == X:
    print('Yes')
else:
    print('No')

# 댜른 분 코드, total에서 뺴는 방법 좋은 것 같다.
import sys
input = sys.stdin.readline
total = int(input())
for i in range(int(input())):
    a, b = map(int, input().split())
    total -= a*b
print("Yes" if total == 0 else "No")

## 예제 입력
# 260000
# 4
# 20000 5
# 30000 2
# 10000 6
# 5000 8
## 예제 출력
# Yes