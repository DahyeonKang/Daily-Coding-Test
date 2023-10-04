## 문제 : 뚤째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

# 내코드 - 실패:시간초과 오류
# import sys
# N = int(input())
# card = [*map(int, sys.stdin.readline().split())]  # 상근 보유
# M = int(input())
# num = [*map(int, sys.stdin.readline().split())]  # 비교할 숫자
# result = ""
# for i in num:
#     result += str(card.count(i))+" "
# print(result)


# 내코드 - 성공:Counter 함수 사용
import sys
from collections import Counter

N = int(input())
card = [*map(int, sys.stdin.readline().split())]  # 상근 보유
M = int(input())
num = [*map(int, sys.stdin.readline().split())]  # 비교할 숫자

c = Counter(card)
for i in num:
    print(c[i], end=' ')


# 다른 분 코드 - bisect를 이용한 이분탐색
import sys
from bisect import bisect_left, bisect_right

def bisearch(x, left, right):
    l = bisect_left(x, left)
    r = bisect_right(x, right)
    return r - l

input = sys.stdin.readline
N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
candidate = list(map(int, input().split()))

for i in range(M):
    print(bisearch(cards, candidate[i], candidate[i]), end=' ')


# 다른 분 코드 - 이분탐색
import sys

input = sys.stdin.readline
N = int(input())
cards = sorted([*map(int, input().split())])
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1


def binarySearch(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid + 1, end)
    else:
        return binarySearch(arr, target, start, mid - 1)

for target in candidate:
    print(binarySearch(cards, target, 0, len(cards) - 1), end=" ")