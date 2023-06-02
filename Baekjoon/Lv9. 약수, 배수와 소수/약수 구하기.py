## 문제 : 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.

import sys
n, k = map(int, sys.stdin.readline().split())
try:
    print([i for i in range(1, n+1) if n%i==0][k-1])
except:
    print(0)

# 다른 분 코드
a,b=map(int,input().split())
print(([f'{i}'for i in range(1,a+1)if a%i<1]+[0]*10000)[b-1])