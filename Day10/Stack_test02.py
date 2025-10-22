# 스택 연습문제 교재 151p
# 문제 09 10진수를 2진수로 변환하기
# 10진수 decimal을 받아 2진수로 변환하고 이를 문자열로 반환하는 solutioin() 함수를 구현하세요

def solution(decimal):
    stack = []  # 변환된 2진수 넣을 스택 리스트 선언 

    while decimal > 0:  # 10진수가 0이상일때까지 반복
        n = decimal%2      # 10진수를 나눈 나머지 n
        stack.append(str(n))    # n을 스택에 push
        decimal //= 2   # 10진수를 2로 나눠준다

    binary = ""     # 2진수를 문자열로 표현할 변수 binary
    while stack:    # 스택이 존재할때까지 반복
        binary += stack.pop()   # stack 전체 pop해서 binary에 추가

    return binary

decimal = 27
print(solution(decimal))