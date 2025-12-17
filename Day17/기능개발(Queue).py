# 큐 문제 16 기능 개발
# 기능 개선 작업 진행 중, 각 기능은 진도가 100% 일 때 서비스에 반영 가능
# 각 기능의 개발속도가 다르므로 뒤의 기능이 앞의 기능보다 먼저 개발 될 수도 있음, 
# "이때 뒤에기능은 앞의 기능이 배포될때 함께 배포되어야함" - * 키 포인트!!
# 배포 순서대로 작업 진척률이 적힌 progresses, 각 작업의 개발 속도가 적힌 정수 배열 speeds 주어질때
# 각 배포마다 몇 개의 기능이 배포되는지 반환하는 solution() 완성

from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    days = 0    # 경과된 날짜 수
    cnt = 0     # 현재 배포 묶음에 포함될 기능 개수

    # 개발이 완료되지 않은 기능이 없어질때까지 반복
    while progresses:

        # 첫번째 기능이 개발 완료 되었을때
        if (progresses[0] + days * speeds[0]) >= 100:
            # 배포 가능하므로 배포개수 1 추가
            cnt += 1

            # 완료된 기능, 스피드는 제거
            progresses.pop(0)
            speeds.pop(0)

        # 기능 개발이 완료 되지 않았을때,
        else:

            # 이미 완료된 기능이 있다면 지금까지 완료된 기능 answer에 추가
            if cnt > 0:
                answer.append(cnt)

                # 다음 배포를 위해 초기화
                cnt = 0
            
            else:
            # 아직 배포할 기능이 하나도 없으면 하루 경과
                days += 1

    # 전체 개발 완료 후 남아있는 마지막 배포 묶음 추가
    answer.append(cnt)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))





