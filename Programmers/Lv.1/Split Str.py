# lv.1 : 문자열 나누기

def mysolution(s):
    answer = 0
    a, b = 0, 0
    x = s[0]

    for i, num in enumerate(s):
        if x == num:
            a += 1
        else:
            b += 1

        if a == b:
            answer += 1
            if i + 1 == len(s):
                return answer
            else:
                x = s[i + 1]  ## x 다시 설정하기

        if i + 1 == len(s):  ## 남은 부분이 없으면
            return answer + 1

    if answer == 0:
        return 1

    return answer


def solution(s):
    answer = 0
    sav1 = 0
    sav2 = 0
    for i in s:
        if sav1 == sav2:
            answer += 1
            a = i
        if i == a:
            sav1 += 1
        else:
            sav2 += 1
    return answer


print(mysolution("abracadabra"))
print(solution("abracadabra"))