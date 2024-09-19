## 문제 : 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록


# 효율성 검사 실패 코드
def solution(phone_book):
    phone_book.sort(key = lambda x: (x[0], len(x)))
    for i in range(len(phone_book)-1):
        temp = phone_book[i]
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(temp):
                return False
    return True


# zip을 사용해 for문을 1개로 줄인 코드
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):   # startswith : 괄호 안의 문자열이 앞 문자열의 접두사인지 확인해 boolean으로 반환
                                # endswith :               ''             접미사인지 확인해 boolean으로 변환
            return False
    return True


# 정렬 사용한 코드
# 내가 이전에 했던 코드 실패 이유 : 문자열 sort는 숫자 정렬처럼 정렬되는 줄 알고, key값으로 첫번째 값 기준으로만 정렬했다.
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
                return False
    return True



# hash 이용한 코드
def solution(phone_book):
    hash_map = {}
    for nums in phone_book:
        hash_map[nums] = 1

    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num
            if arr in hash_map and arr != nums:
                return False
    return True