## 문제 : 첫째 줄에 형택이의 곱셈 결과를 출력한다.

# 오류 - 시간초과
a, b = input().split()
a_l = list(map(int, a))
b_l = list(map(int, b))
sum = 0
for i in a_l:
    for j in b_l:
        sum += i * j
print(sum)


# 성공
a, b = input().split()
a_l = list(map(int, a))
b_l = list(map(int, b))
print(sum(a_l) * sum(b_l))