## 문제 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

n = int(input())
prime = []
for i in range(2, n+1):
    if n % i == 0:
        prime.append(i)
        n = n // i
        while True:
            if n % i == 0:
                prime.append(i)
                n = n // i
            else:
                break

print(*prime, sep='\n')


# 다른 분 코드
n = int(input())
i = 2
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
        print(i)
if n > 1:
    print(n)

# 다른 분 코드
n=int(input())
for i in range(2,int(n**(0.5))+2):
    while n%i==0:print(i);n//=i
if n!=1:print(n)