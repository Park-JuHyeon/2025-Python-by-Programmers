# 큐 문제 17 카드뭉치
# 영어 단어가 적힌 카드 뭉치 2개로 규칙을 사용해 원하는 순서의 단어 배열 만들 수 있는지
# 규칙 : 1. 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다
# 2. 한 번 사용한 카드는 다시 사용할 수 없습니다.
# 3. 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.
# 4. 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.
# ex) cards1 = ["i", "drink", "water"], cards2 = ["want", "to"]
# goal = ["i", "want", "to", "drink", "water"], result = "Yes"

from collections import deque

def solution(cards1, cards2, goal):
    # 각 카드를 데큐로 변환
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    # goal이 존재할때 까지
    while goal:
        # cards1에 문자가 존재하고, front의 값이 goal의 front와 동일하면
        # 각 문자 pop
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()

        # cards2에 문자가 존재하고, front의 값이 goal의 front와 동일하면
        # 각 문자 pop
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()

        # 일치하는 원소 없을 시 종료
        else:
            break
    
    # goal에 값이 남아있으면 No, 비어있으면 Yes 출력
    return "Yes" if not goal else "No"

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))
