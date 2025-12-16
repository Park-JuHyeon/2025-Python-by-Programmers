# 스택 모의테스트, 문제 10 괄호 회전하기 교재 154p
# 올바른 괄호 문자열 : (), [], {}
# 대괄호, 중괄호, 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다.
# 이 s를 왼쪽으로 x(0<=x<(s의 길이)) 만큼 회전시켰을 때 
# s가 올바른 괄호 문자열이 되게 하는 x의 개수 반환하는 solution() 함수 완성하세요

def solution(s):
    
    x = 0
    n = len(s)
    for i in range(n):
        stack = []
        for j in range(n):
            c = s[(i+j) % n]
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    break
            
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    break
        else:
            if not stack:   # 전부다 올바른 괄호일 경우
                x += 1

    return x

s = "}]()[{"
print(solution(s))


