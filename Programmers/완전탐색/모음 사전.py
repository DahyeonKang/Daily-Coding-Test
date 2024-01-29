## 문제 : 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록

from itertools import product
def solution(word):
    answer = 0
    P = []
    original = list('AEIOU')
    for i in range(1, len(original) + 1):
        for p in product(original, repeat=i):
            P.append("".join(p))

    P = sorted(list(set(P)))
    answer = P.index(word) + 1
    return answer

# print(solution("AAAAE"))


# 의문 ?
# 문자열을 sort()한 결과와 sorted()한 결과가 다르다.
# sort()   : ['A', 'E', 'I', 'O', 'U', 'AA', 'AE', 'AI', 'AO', 'AU', 'EA', ...
# sorted() : ['A', 'AA', 'AAA', 'AAAA', 'AAAAA', 'AAAAE', 'AAAAI', 'AAAAO', ...


# 내코드랑 비슷한데, sort()하니까 잘 되는 코드 . .?
from itertools import product
def solution(word):
    answer = []
    li = ['A', 'E', 'I', 'O', 'U']
    for i in range(1,6):
        for per in product(li,repeat = i):
            answer.append(''.join(per))
    answer.sort()
    print(answer)
    return answer.index(word)+1

print(solution("AAAAE"))