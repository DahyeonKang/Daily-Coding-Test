## 문제 : 수에 대하여 최소공배수를 구하는 프로그램을 작성

A, B = map(int, input().split())
result = A*B
while B>0:
    A,B = B, A%B
print(result//A)