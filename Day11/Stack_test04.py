# 문제 11 짝지어 제거하기
# 알파벳 소문자로 구성된 문자열에서 같은 알파벳이 2개 붙어있는 짝 찾기
# 짝을 찾은 후 그 둘을 제거한 뒤 앞뒤로 문자열을 이어붙임
# 과정 반복 후 문자열을 모두 제거하면 종료
# 짝지어 제거하기를 성공적으로 수행 가능하면 1, 못하면 0 출력

def solution(s):
    x = 0
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if not stack:
        x = 1
    else:
        x = 0
    return int(not stack)

s = "baabaa"
print(solution(s))