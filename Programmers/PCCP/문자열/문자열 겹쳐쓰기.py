## 문제 : 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을
# 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.


def solution(my_string, overwrite_string, s):
    my_string = list(my_string)
    for i in range(len(overwrite_string)):
        my_string[ s +i] = overwrite_string[i]

    return ''.join(my_string)

# 강사님 코드
def solution(my_string, overwrite_string, s):
    start = my_string[0 : 5]
    end = my_string[s + len(overwrite_string)]
    answer = start + overwrite_string + end
    return answer
