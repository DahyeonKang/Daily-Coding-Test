## 문제 : 첫째 줄에 B진법 수 N을 10진법으로 출력한다.

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = input().split()
answer = 0
for i, num in enumerate(n[::-1]):
    answer += int(b) ** i * num_list.index(num)
print(answer)

# 간단한 코드
n, b = input().split()
print(int(n, int(b)))

# 응용 : 10진수를 2진수로 변환
bin(int(n))