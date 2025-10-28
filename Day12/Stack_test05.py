# p162 문제 12 주식가격
# 초 단위로 기록된 주식 가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 반환하도록 solution 함수 완성하세요

def solution(prices):
    # 스택의 0번째값을 미리 넣어 초기화
    # 스택에는 "가격이 아직 떨어지지 않은 시점의 인덱스"가 저장됨
    stack = [0]
    n = len(prices)
    # 각 시점별로 "가격이 떨어지지 않은 기간(초)"을 저장할 배열
    answer = [0] * n

    for i in range(1, n):  
        # 현재 시점의 주가(prices[i])가 스택 맨 위 인덱스의 주가보다 낮다면
        # → 주가가 떨어졌다는 의미
        while stack and prices[i] < prices[stack[-1]]:
            # 가격이 떨어지기 전의 시점 j를 스택에서 꺼냄
            j = stack.pop()
            # j 시점부터 i 시점까지는 주가가 유지되거나 상승했음
            # 주가가 떨어진 시점 i에서 기간 계산
            answer[j] = i - j

        # 현재 시점 i를 스택에 추가 (아직 주가가 떨어지지 않음)
        stack.append(i)

    # 모든 시점에 대해 반복이 끝난 후에도
    # 스택에 남아 있는 인덱스들은 끝까지 가격이 떨어지지 않은 경우임
    while stack:
        j = stack.pop()
        # 마지막 시점(n-1)까지 유지되었으므로 기간은 (마지막 인덱스 - 현재 인덱스)
        answer[j] = n -1 - j 

    return answer

prices = [1,2,3,2,3]
# return = [4,3,1,1,0]
print(solution(prices))