# lv.1 : 과일 장수

def mysolution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    l = [score[i:i+m] for i in range(0, len(score), m)]
    for i in l:
        if len(i) == m:
            answer += min(i) * m
    return answer


def solution(k, m, score):
    return sum(sorted(score)[len(score) % m::m])*m

# list의 extended slices [a::b] : index a부터 b 간격으로


print(mysolution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
