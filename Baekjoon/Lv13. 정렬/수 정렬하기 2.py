## 문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import time
import sys

## 0.45230913162231445 - 실패
start = time.time()
N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))
l.sort()
print(*l, sep='\n')
end = time.time()
print(end-start)

## 0.30640244483947754
start = time.time()
N = int(sys.stdin.readline())
l = [int(sys.stdin.readline().strip()) for _ in range(N)]
print(*sorted(l), sep='\n')
end = time.time()
print(end-start)

## 0.38498806953430176
start = time.time()
N = int(sys.stdin.readline())
l = []
for _ in range(N):
    l.append(int(sys.stdin.readline()))
l.sort()
print(*l, sep='\n')
end = time.time()
print(end-start)

## 0.28788304328918457 - 성공
start = time.time()
N = int(sys.stdin.readline())
li = [0] * N
for i in range(N):
    li[i] = int(sys.stdin.readline())
print(*sorted(li), sep='\n')
end = time.time()
print(end-start)

# 다른 분 코드
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')

# 다른 분 코드
n = int(input())
data = sorted(map(int, sys.stdin.read().splitlines()))
    # sys.stdin.read().splitlines() : 파일의 끝까지 한번에 읽어오고 개행문자를 제외하여 리스트로 읽는다.
print(data)
print("\n".join(map(str,data)))

# 다른 분 코드
print('\n'.join(map(str, sorted(list(map(int, sys.stdin.read().split()))[1:]))))

# 이외에도 미리 범위의 수에 대해 None 리스트([None, None, None, ...])를 만들어 거기에 대입한 코드도 있음
a=[None]*2000001
b=map(int, open(0))
next(b)
print(b)
for i in b:
    a[i] = 1
print("\n".join(str(i) for i in range(-1000000, 1000001, 1) if a[i]))
