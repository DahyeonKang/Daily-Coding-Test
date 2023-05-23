## 문제 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

from collections import Counter
s = input()
dict = Counter(s.upper())
count = [k for k, v in dict.items() if v == max(dict.values())]
print('?' if len(count)>1 else count[0])