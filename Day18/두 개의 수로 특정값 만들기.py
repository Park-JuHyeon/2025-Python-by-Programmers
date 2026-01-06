# 문제 18 두 개의 수로 특정값 만들기

# - 양의 정수로 이루어진 리스트 arr와 정수 target이 주어졌을 때,
# - 이 중에서 합이 target인 두 수가 arr에 있는지 찾으시오.
# - 있으면 True, 없으면 False를 반환하는 solution() 함수 작성

# - ex) arr = [1,2,4,8], target = 6, return = True

def solution(arr, target):
    hash = [0] * (target + 1)

    for num in arr:
        if num <=target:
            hash[num] = 1

    for num in arr:

        if (num >= target):
            continue

        if ((target - num) == num):
            continue

        if(hash[target - num]):
            return True

    return False

arr = [1,2,3,4,8]
target = 6
print(solution(arr, target))