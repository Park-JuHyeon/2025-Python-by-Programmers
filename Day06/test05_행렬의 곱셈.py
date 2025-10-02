# 교재 121 배열 문제 05 행렬의 곱셈
# 2차원 행렬 arr1과 arr2를 입력받아 arr1에 arr2를 곱한 결과를 반환하는 solution() 함수를 완성
# 행렬곱셈 방법 : ret[0][0] = (arr1[0][0]*arr2[0][0] + arr1[0][1]*arr2[1][0] + arr1[0][2]*arr2[2][0])

def solution(arr1, arr2):
    
    # 각 행렬의 길이 변수 선언
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    # 결과값 담을 리스트 선언
    ret = [[0] * c2 for _ in range(r1)]

    for i in range(r1): 
        for j in range(c2):
            for k in range(c1):
                ret[i][j] += arr1[i][k] * arr2[k][j]
    return ret

arr1 = [[2,3,2],[4,2,4],[3,1,4]]
arr2 = [[5,4,3],[2,4,1],[3,1,1]]
print(solution(arr1, arr2))