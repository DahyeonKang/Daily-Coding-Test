## 문제 : 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

N = int(input())
v_list = list(map(int, input().split()))
find = int(input())
print(v_list.count(find))

## 입력
# 11
# 1 4 1 2 4 2 4 2 3 4 4
# 2
## 출력
# 3
