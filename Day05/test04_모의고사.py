# 프로그래머스 문제 모의고사
# 교재 117p

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

def solution(answers):
    # 수포자들의 패턴 미리 리스트에 저장
    patterns = [[1,2,3,4,5],
                [2,1,2,3,2,4,2,5],
                [3,3,1,1,2,2,4,4,5,5]]
    
    # 수포자들의 패턴을 답안과 비교해 일치하는 개수 칭하는 scores 리스트 선언
    scores = [0] * 3

    # 각 수포자의 패턴과 정답이 얼마나 일치하는지 확인
    for i, answer in enumerate(answers):    # i는 answer의 인덱스, answer는 실제값
        for j, pattern in enumerate(patterns):  # 수포자들의 패턴을 도는 반복문
            # 정답 패턴의 길이가 수포자의 답안 길이보다 긴 경우 정답패턴의 처음 데이터와 다시 비교
            if answer == pattern[i % len(pattern)]:     # pattern의 [0]번째 값, [1]번째값...
                scores[j] += 1
    
    max_score = max(scores) # 수포자 중 가장 높은 점수 저장

    highest_scores = []     # 가장 높은 점수 받은 수포자들의 번호 리스트 저장
    for i, score in enumerate(scores):  # 수포자들 점수 리스트를 도는 반복문
        if score == max_score:          
            # 가장 높은 점수 받은 수포자 번호 추가, i는 0부터라서 +1
            highest_scores.append(i + 1)  
    return highest_scores

answers = [1,3,2,4,2]
print(solution(answers))

    



