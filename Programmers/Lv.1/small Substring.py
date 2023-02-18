# lv.1 : 크기가 작은 부분문자열

def mysolution(t, p):
    answer = 0
    l = len(p)
    for i in [t[i:i+l] for i in range(0, len(t))]:
        if len(i) == l and int(i) <= int(p):
            answer += 1
    return answer


def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1
    return answer


print(mysolution("3141592", "271"))
print(mysolution("500220839878", "7"))
print(mysolution("10203", "15"))
