## 문제 : before의 순서를 바꾸어 after를 만들 수 있으면 1을,
# 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

def solution(before, after):
    answer = 0
    before = sorted(list(before))
    after = sorted(list(after))
    if  before == after:
        return 1
    else:
        return 0
