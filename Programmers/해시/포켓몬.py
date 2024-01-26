## 문제 :  N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아,
# 그때의 폰켓몬 종류 번호의 개수를 return 하도록


def solution(nums):
    unique = len(set(nums))
    l = len(nums)//2
    if l >= unique:
        return unique
    else:
        return l


# 더 짧은 코드
def solution(nums):
    return min(len(set(nums)), len(nums)/2)