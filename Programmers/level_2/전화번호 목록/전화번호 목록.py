def solution(phone_book):
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


"""
zip -> 튜플로 묶기

A.startswith(B)
 -> A의 첫번째부터 사작하여 B의 단어가 있는지 확인하는 함수
 (optional) startswith(B, _) str[_:]
    B의 범위조절 가능
"""