# 05-5 합격자 모의테스트
# 문제 03 두개 뽑아서 더하기

def solution(numbers):
    n = len(numbers)
    sum_list = []
    for i in range(n):
        for j in range(i+1, n):
            sum_result = numbers[i] + numbers[j]            
            sum_list.append(sum_result)
    sum_list = sorted(set(sum_list))
    return sum_list
     
numbers = [2,1,3,4,1]
print(solution(numbers))