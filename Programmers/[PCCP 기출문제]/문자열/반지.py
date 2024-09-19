## 문제 : 찾고싶은 문자열이 적힌 반지의 개수를 정수 한줄로 출력해주세요.


def solution(wordfind, N, ring):
    answer = 0
    for i in ring:
        if wordfind in i+i:
            answer += 1
    return answer

# 아니면
# if wordfind in i+i:    ->     if wordfind in i * 2
