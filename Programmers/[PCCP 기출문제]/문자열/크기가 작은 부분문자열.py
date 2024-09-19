def solution(t, p):
    answer = 0
    l = len(p)
    newp = int(p)

    for i in range(len(t) - l + 1):
        if int(t[i:i+l]) <= newp:
            answer += 1

    return answer

# print(solution("3141592","271"))
print(solution("500220839878","7"))