# 문제04 모의고사 복습

def solution(answers):
    patterns = [[1,2,3,4,5],
                [2,1,2,3,2,4,2,5],
                [3,3,1,1,2,2,4,4,5,5]]
    scores = [0] * 3

    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):     # pattern은 patterns[0], patterns[1] 이렇게 돈다
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    
    high_score = max(scores)

    highest_score = []

    for i, score in enumerate(scores):
        if score == high_score:
            highest_score.append(i + 1)
    return highest_score

answers = [1,2,3,4,5]
print(solution(answers))