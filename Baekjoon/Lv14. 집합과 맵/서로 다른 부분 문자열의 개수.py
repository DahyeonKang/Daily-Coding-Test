## 문제 : 문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

s = input()
substring = []
l = len(s)
for i in range(1, l+1):
    start = 0
    end = i
    while True:
        if end <= l:
            substring.append(s[start:end])
            start += 1
            end += 1
        else:
            break

print(len(set(substring)))


# 다른 분 코드: 부분문자열 구하는 함수 생성
from sys import stdin
input = stdin.readline

def getSubset(s, n):
  subset = set()
  for i in range(len(s)-n+1):
    subset.add(s[i:i+n])
  return subset

s = input().rstrip()
cnt = 0
for i in range(1, len(s)+1):
  cnt += len(getSubset(s, i))
print(cnt)
