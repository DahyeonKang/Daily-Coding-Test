## 문제 : 자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오.

a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
diff = set(A) ^ set(B)
print(len(diff))


# 다른 분 코드 : 대칭차집합 정의를 이용한 풀이
import sys
input = sys.stdin.readline
a,b = map(int,input().split())
cnt = 0
A = set(input().split())
for i in input().split():
    if i in A:
        cnt+=1
print(a+b-cnt*2)