# 문제 06 : 실패율      p124, 난이도 별 2
# - N = 5, stages = [2,1,2,6,2,4,3,3], result = [3,4,2,1,5]

# - 1번 스테이지는 총 8 명 사용자가 도전, 1명이 클리어 실패
#     - 1번 스테이지 실패율 : 1/8
# - 2번 스테이지 총 7명 도전, 3명 실패
#     - 2번 스테이지 실패율 : 3/7
# - 3번 스테이지 총 4명 도전, 2명 실패
#     - 3번 스테이지 실패율 : 2/4
# - 4번 스테이지 실패율 : 1/2
# - 5번 스테이지 실패율 : 0/1

# - 각 스테이지 번호를 실패율로 내림차순하면 [3,4,2,1,5] 가 됨

def solution(N, stages):
    # 스테이지별 도전자 수 구함
    chellenger = [0] * (N+2)    # N+1번째 인덱스의 값을 저장하기위해 N+2 까지 배열 생성   
    for stage in stages:
        chellenger[stage] += 1

    # 스테이지별 실패한 사용자 수 계산
    # 각 스테이지별 실패율을 저장할 딕셔너리
    fails = {}
    total = len(stages)

    # 각 스테이지 순회하며 실패율 계산
    for i in range(1, N+1):  # stage 개수 만큼 반복
        # 스테이지에 도전자가 없으면 실패율도 0
        if chellenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = chellenger[i] / total
            total -= chellenger[i]

    # 실패율 높은 스테이지부터 내림차순 정렬
    # fails 딕셔너리의 key(스테이지 번호)를 실패율 값(fails[x]) 기준으로 정렬
    result = sorted(fails, key=lambda x : fails[x], reverse=True)   

    return result

N = 5
stages = [2,1,2,6,2,4,3,3]
print(solution(N, stages))