## 문제 : 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

s = input()
alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in alpha:
    if i in s:
        s = s.replace(i, " ")
print(len(s))

# 다른 분 코드
word = input()
lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in lst:
    word = word.replace(i,'*')
print(len(word))
