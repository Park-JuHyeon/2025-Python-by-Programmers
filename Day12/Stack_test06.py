# 스택 문제13 크레인 인형 뽑기 게임 p169, 권장 시간복잡도 : O(N^2 + M)
# N X N 으로 구성된 격자, 크레인은 좌우로 움직일 수 있고, 멈춘위치의 가장 위에 있는 인형을 집어올린다
# 같은 모양의 인형 2개가 바구니에 연속으로 쌓이면 두 인형이 사라진다.
# 인형이 없는 곳에서 크레인을 작동시키면 아무일도 일어나지 않는다
# 2차원 배열 board와 인형을 집는 크레인을 작동시킨 위치가 담긴 배열 moves가 주어질때,
# 크레인을 모두 작동시킨 후 사라진 인형개수를 반환하는 solution 구현

def solution(board, moves):
    # 순서대로 인형을 저장할 스택 lanes board 개수만큼 선언
    lanes = [[] for _ in range(len(board[0]))]

    # 마지막 배열이 가장 밑으로 가야하기 때문에 역방향으로 반복문 생성
    for i in range(len(board)-1, -1, -1):
        # board의 수만큼 반복
        for j in range(len(board[0])):
            # board[i][j]값이 0이 아니면
            if board[i][j]:
                # lanes 스택에 값 저장
                lanes[j].append(board[i][j])
    
    # 뽑은 인형을 저장할 바구니 스택 선언
    bucket = []
    # 사라진 인형 개수 저장할 변수 초기화
    result = 0
    # 크레인의 이동 시작
    for m in moves:
        # lanes 스택의 m번째에 값이 있을경우
        if lanes[m-1]:
            # 인형번호 저장
            doll = lanes[m-1].pop()

            # 바구니에 인형이 존재하고, 가장 top의 인형이 새로뽑은 doll과 같은 번호이면
            if bucket and bucket[-1] == doll:
                # top의 바구니 인형 사라짐(pop)
                bucket.pop()
                # 사라진 인형수만큼(언제나2개) 결과에 +2
                result += 2

            # 바구니에 인형이 없고, 뽑은 인형이 다를경우 바구니에 doll 번호 푸시
            else:
                bucket.append(doll)

    return result

# board의 1~100 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 의미
board = [[0,0,0,0,0], [0,0,1,0,3], [0,2,5,0,1], [4,2,4,4,2], [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))



