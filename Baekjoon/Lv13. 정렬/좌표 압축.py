## 문제 : 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

# 내 코드 - 시가 초과 이유로 다른 아이디어 코드 사용
# 아이디어 : 입력받은 수 리스트(1) 중복 제거(2) -> 정렬(3) -> 원본 수 리스트(1)를 key로 하고 (3)을 value로 해 값을 찾는다.
import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
li = sorted(set(num))
dict = {li[i]: i for i in range(len(li))}
for i in num:
    print(dict[i], end=" ")


# 내 코드 - 시간 초과 실패
# import sys
# N = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
# setli = list(set(li))
# comp = [len(list(filter(lambda x: x<i, setli))) for i in li]
# print(*comp, sep=' ')

