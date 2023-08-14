## 알고리즘 수업 - 알고리즘의 수행 시간 1

# MenOfPassion(A[], n) {
#     i = ⌊n / 2⌋;
#     return A[i]; # 코드1
# }
n = int(input())
print("1\n0")

# 다른 분 코드 : n을 입력받지 않고 출력만 했다.
print("1\n0")


## 알고리즘 수업 - 알고리즘의 수행 시간 2

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         sum <- sum + A[i]; # 코드1
#     return sum;
# }
n = int(input())
print(n)
print(1)

# 다른 분 코드
print(input(), 1)


## 알고리즘 수업 - 알고리즘의 수행 시간 3
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
n = int(input())
print(n*n)
print(2)

# 다른 분 코드
print(int(input()) ** 2)
print(2)


## 알고리즘 수업 - 알고리즘의 수행 시간 4
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
n = int(input())
print(int(n*(n-1)/2))
print(2)

# 다른 분 코드
n=int(input())
print(n*(n-1)//2, 2, sep='\n')
# 다른 분 코드
a = int(input())
print((a*(a-1))//2)
print(2)


## 알고리즘 수업 - 알고리즘의 수행 시간 5
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }
n = int(input())
print(n**3)
print(3)


## 알고리즘 수업 - 알고리즘의 수행 시간 6
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }
n = int(input())
sum = 0
for i in range(1, n-1):
    sum += i * (i + 1) // 2
print(sum)
print(3)

# 다른 분 코드
n = int(input())
print(((n-1) * (n-2) * 2 * n) // 12)
print(3)
# 다른 분 코드 : nC3 = n!/(3!(n-3)!) = n(n-1)(n-2)/3*2*1 = n(n-1)(n-2)/6.
N = int(input())
print((N * (N - 1) * (N - 2)) // 6)
print(3)


## 알고리즘 수업 - 점근적 표기 1
## 문제 : f(n), c, n0가 O(n) 정의를 만족하면 1, 아니면 0을 출력한다.
# f(n) = a1n + a0
# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if (a1*n0 + a0 <= c*n0) and (a1<=c):
    print(1)
else:
    print(0)

# 틀린 코드
# if a1 < c:
#     if a0/(c-a1) <= n0:
#         print(1)
#     else:
#         print(0)
# elif a1 > c:
#     print(0)
# else:  # a1==c
#     if a0 == 0:
#         print(1)
#     else:
#         print(0)

# 다른 분 코드
a, b, c, d=map(int, open(0).read().split())
print(+(a+b/d <= c >= a))

# 다른 분 코드
a,b=map(int,input().split())
c,d=int(input()),int(input())
print(1 if a*d+b<=c*d and a<=c else 0)




