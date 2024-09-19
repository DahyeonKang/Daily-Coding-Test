


# 런타임 에러 
from itertools import permutations
def solution(jobs):
    answer = 1000
    n = len(jobs)
    for a, b, c in permutations(range(n), n):
        time = (3*jobs[a][1] + 2*jobs[a][0] + 2*jobs[b][1] - jobs[b][0] + jobs[c][1] - jobs[c][0]) // 3
        if answer > time:
            answer = time
    return answer