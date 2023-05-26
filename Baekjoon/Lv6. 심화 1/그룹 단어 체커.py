## 문제 : 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# import re
#
# n = int(input())
# count = 0
#
# for _ in range(n):
#     l = []
#     word = input()
#     breaker = 0
#     for s in set(word):
#         if word.count(s) > 1:  # 중복된 문자가 있다면
#             idx = [i.start() for i in re.finditer(s, word)]  # 인덱스 위치를 찾고
#             for a1, a2 in zip(idx, idx[1:]):  # 연속된 문자인지 비교한다.
#                 if a1+1 == a2:
#                     pass
#                 else:
#                     breaker = True
#                     break
#         if breaker == True:
#             break
#     if breaker != True:
#         count += 1
# print(count)


# 다른 분 코드 : 각 문자열 종류들이 처음 위치한 곳으로 정렬하면, 그룹끼리 묶여진다. 이 결과랑 기존 문자열이랑 비교하면 그룹 유무를 알 수 있다.
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)

# 다른 분 코드
N = int(input())
cnt = N
for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)