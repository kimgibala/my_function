"""
코드 작성 일자 : 2023년 10월 23일
코드 작성자 : 김기환
코드 이름 : utils.py
코드 목적 : 유용한 함수를 따로 저장하여 두고 나중에 물러와 사용하기 위함
"""


def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x-1)


def gugudan(x):
    for i in range(9):
        print((i+1)*x)
