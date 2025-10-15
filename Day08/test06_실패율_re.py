# 문제06 실패율 복습

def solution(N, stages):
    chellenger = [0] * (N+2)
    for i in stages:
        chellenger[i] += 1

    fails = {}
    num = len(stages)

    for i in range(1, N+1):
        if chellenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = chellenger[i]/num
            num -= chellenger[i]
        
    result = sorted(fails, key= lambda x : fails[x], reverse=True)

    return result

stages = [2,1,2,6,2,4,3,3]
N = 5
print(solution(N, stages))