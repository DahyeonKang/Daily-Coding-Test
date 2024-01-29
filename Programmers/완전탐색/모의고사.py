## 문제 : 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return


def solution(answers):
    answer = []
    A = [1, 2, 3, 4, 5] * 2000
    B = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    acount, bcount, ccount = 0, 0, 0

    for i, a, b, c in zip(answers, A, B, C):
        if i == a:
            acount += 1
        if i == b:
            bcount += 1
        if i == c:
            ccount += 1

    maxnum = max(acount, bcount, ccount)
    if maxnum == acount:
        answer.append(1)
    if maxnum == bcount:
        answer.append(2)
    if maxnum == ccount:
        answer.append(3)
    return answer


# 더 짧은 코드 - 나는 10000개 제한이 있는 정답 길이에 대해 학생들의 패턴을 곱했지만, 나누기를 활용해 인덱스 반복으로 구현 가능
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]