# 문제 15 요세푸스문제

# - N명의 사람이 원 형태로 서 있습니다. 각 사람은 1부터 N까지 번호표를 갖고 있습니다.
# 그리고 임의이ㅡ 숫자 K가 주어졌을 때 다음과 같이 사람을 없앱니다.

# - 1번 번호표를 가진 사람을 기준으로 K번째 사람을 없앱니다.
# - 없앤 사람 다음 사람을 기준으로 하고 다시 K번째 사람을 없앱니다.

# - N과 K가 주어질 때 마지막에 살아있는 사람의 번호를 반환하는 solution 함수 구현

# - ex) N = 5, K = 2
from collections import deque

def solution(N, K):
    # 1 ~ N까지의 번호 deque에 추가
    Queue = deque(range(1, N+1))

    # Queue의 개수가 한개 남을때 까지 반복 수행
    while len(Queue) > 1:
        # K번째 요소 찾기 위해 앞에서부터 제거한 값을 맨뒤에 다시 추가하는 작업
        for _ in range(K-1):
            Queue.append(Queue.popleft())
        
        # 가장 앞으로온 K번째 요소 제거
        Queue.popleft()

    # 마지막 남은 큐 요소 리턴
    return Queue[0]

N = 5
K = 3
print(solution(N,K))




