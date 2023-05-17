## 문제 : 알파벳 소문자의 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.


import string

s = input()
alpha = string.ascii_lowercase
l = []
for i in alpha:
    if i in s:
        l.append(s.index(i))
    else:
        l.append(-1)
print(*l)

# 다른 분 코드 : 정수를 아스키코드로 바꿔주는 방법을 이용해 위치를 찾는 방법
s = input()
for i in range(97, 123):  # a 부터 z 까지
    print(s.find(chr(i)), end=' ')