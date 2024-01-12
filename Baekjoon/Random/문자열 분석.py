## 문제 : 첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.

import sys
while True:
    string = sys.stdin.readline().rstrip('\n')
    if not string:
        break
    low = sum([True for s in string if s.islower()])
    up = sum([True for s in string if s.isupper()])
    digit = sum([True for s in string if s.isdigit()])
    space = sum([True for s in string if s.isspace()])
    print(low, up, digit, space)


# 아래 코드는 블로그에 많이 나와있는데 파이참에서는 계속 입력받게 됨
# import sys
# while True:
#     try:
#         string = sys.stdin.readline()
#         low = sum([True for s in string if s.islower()])
#         up = sum([True for s in string if s.isupper()])
#         digit = sum([True for s in string if s.isdigit()])
#         space = sum([True for s in string if s.isspace()])
#         print(low, up, digit, space)
#     except EOFError:
#         break


# import sys
#
# string = sys.stdin.readlines()
# for str in string:
#     low = sum([True for s in str if s.islower()])
#     up = sum([True for s in str if s.isupper()])
#     digit = sum([True for s in str if s.isdigit()])
#     space = sum([True for s in str if s.isspace()])
#     print(low, up, digit, space)
