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


