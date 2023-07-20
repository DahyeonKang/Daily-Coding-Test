## 문제 : 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

m = int(input())
n = int(input())
primeL = []

for i in range(m, n+1):
    if i != 1:
        for j in range(2, i + 1):
            if i % j == 0:
                if j == i:
                    primeL.append(i)
                break
if sum(primeL) != 0:
    print(sum(primeL))
    print(min(primeL))
else:
    print(-1)
