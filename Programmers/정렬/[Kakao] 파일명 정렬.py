## 문제 : 파일명을 정해진 규칙에 따라 정렬하는 프로그램을 작성하라


import re
def solution(files):
    f_low = list(map(lambda x: x.lower(), files))
    f_split = [re.split(r"([0-9]+)", i) for i in f_low]
    d = dict(zip(range(len(f_split)), f_split))
    d_sort = dict(sorted(d.items(), key=lambda x: (x[1][0], int(x[1][1]))))
    answer = [files[idx] for idx in d_sort.keys()]
    return answer


## head, number, tail을 생성하는 코드 시도
# import re
# def solution(files):
#     answer = []
#     files = list(map(lambda x:x.lower(), files))
#     splitFile = [re.split(r"([0-9]+)", i) for i in files]

#     header = ([splitFile[i][0] for i in range(len(splitFile))])
#     number = ([splitFile[i][1] for i in range(len(splitFile))])
#     # tail = ([splitFile[i][2:] if splitFile[i][2:] else "" for i in range(len(splitFile)) ])
#     print(header, number)
#     print(splitFile)
#     if len(set(header)) == 1 :
#     else :
#         header.sort()
#     return answer


## 전체적인 정렬은 구현했지만 대소문자를 구분하는 코드가 필요함
# import re
# import numpy as np
# def solution(files):
#     answer = []
#     F_low = list(map(lambda x:x.lower(), files))
#     F_split = [re.split(r"([0-9]+)", i) for i in F_low]
#     F_split.sort(key=lambda x:(x[0], int(x[1])))
#     print(F_split)
#     F_sort = ["".join(i) for i in F_split]
#     print(F_sort)
#     return answer
