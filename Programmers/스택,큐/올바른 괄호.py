## 문제 : 문자열 s가 올바른 괄호이면 true를 return 하고,
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.


# 런타임 에러 난 코드
# def solution(s):
#     answer = True
#     s = list(s)
#
#     while answer and s:
#         before_s = s.copy()
#         i = 0
#         while i < len(s)-1:
#             if s[i] != s[i + 1]:  # 앞뒤가 다르다면
#                 if s[i] == '(' and s[i + 1] == ')':
#                     s.pop(i)
#                     s.pop(i)
#                     break
#             i += 1
#         if before_s == s:
#             answer = False
#             break
#     return answer


# 다른 사람 풀이
def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

# print(solution(")()("))
print(solution("()()"))

