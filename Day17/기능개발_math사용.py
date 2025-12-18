# 교재 풀이 버전 math 함수 사용

import math

def solution(progresses, speeds):
    answer = []
    n = len(progresses)

    # ceil 함수 : 소수점을 올림 연산하는 함수
    days_left = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(n)]

    count = 0
    max_day = days_left[0]

    for i in range(n):
        if days_left[i] <= max_day:
            count +=1
        
        else:
            answer.append(count)
            count = 1
            max_day = days_left[i]

    answer.append(count)


    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))


