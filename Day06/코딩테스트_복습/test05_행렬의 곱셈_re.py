# test05_ 행렬의 곱셈 복습

def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    ret = [[0] * c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                ret[i][j] += arr1[i][k] * arr2[k][j]    

    return ret

arr1 = [[2,3,2],[4,2,4],[3,1,4]]
arr2 = [[5,4,3],[2,4,1],[3,1,1]]

print(solution(arr1, arr2))