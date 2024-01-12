## 문제 : 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(sorted(array[c[0]-1 : c[1]])[c[2]-1])
    return answer