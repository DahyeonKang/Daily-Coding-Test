## 문제 : 세 자리 수를 거꾸로 읽는 사람의 입장에서 큰 수를 구하는 프로그램을 작성하시오.

a, b = input().split()
a = a[2]+a[1]+a[0]
b = b[2]+b[1]+b[0]
print(a if a>b else b)

# 다른 분 코드
print(max(input()[::-1].split()))