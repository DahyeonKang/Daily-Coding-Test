## 문제 : 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

s = input()
print(1 if s[::-1] == s else 0)

# 다른 분 코드
alp =list(str(input()))
if list(reversed(alp)) == alp:
    print(1)
else:
    print(0)