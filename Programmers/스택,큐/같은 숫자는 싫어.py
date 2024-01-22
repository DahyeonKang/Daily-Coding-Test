## 문제 : 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.


def solution(arr):
    answer = []
    count = 0
    l = len(arr)
    arr = arr[::-1]
    while count < l:
        count += 1
        if count == 1:
            answer.append(arr.pop())
        else:
            temp = arr.pop()
            if temp != answer[-1]:
                answer.append(temp)

    return answer


# 다른 분 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a