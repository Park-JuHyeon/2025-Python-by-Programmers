# 스택 문제 08 괄호 짝 맞추기 p146
# '(' , ')' 의 짝이 맞는지 판별하는 solution

def solution(s):
    # 스택선언
    stack = []

    # 문자열 s를 탐색하는 반복문
    for i in s:
        if i == "(":
            # 열린괄호는 append
            stack.append(i)
        elif i == ")":
            if not stack:
                # 처음부터 닫힌괄호가 나오면 안됨
                return False
            else: 
                # 열린괄호 뒤 닫힌괄호가 나오면 pop
                stack.pop()

    if stack:
        # 스택에 값이 남아있으면 안됨
        return False
    else:
        return True
    
s = ")()("
s2 = ")()("
print(solution(s))