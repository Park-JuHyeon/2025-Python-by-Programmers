def solution(arr):
    answer = []
    answer.append(arr[0])
    now = arr[0]

    for i in arr:
        if i != now:
            answer.append(i)
            now = i

    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))