# 스택 문제 14 표 편집 (고난이도) p177
# 명령어 기반 표의 행을 선택, 삭제, 복구하는 프로그램 작성
# "U X" : 현재 선택한 행에서 X칸 위에 있는 행 선택
# "D X" : 현재 선택한 행에서 X칸 아래에 있는 행 선택
# "C" : 현재 선택한 행을 삭제한 후, 바로 아래 행을 선택 (단 삭제된 행이 가장 마지막 행인 경우 바로 윗행 선택)
# "Z" : 가장 최근에 삭제한 행을 원래대로 복구 (단 현재 선택한 행은 바뀌지 않습니다.)

# 처음 표의 행 개수를 나타내는 정수 n, 처음 선택한 행의 위치 정수 k
# 수행한 명령어가 담긴 문자열 배열 cmd 주어질때
# 모든 명령어 수행 후 표의 상태와 처음 표의 상태 비교, 삭제되지 않은 행 "O", 삭제된 행 "X" 반환

def solution(n, k, cmd):
    # 삭제된 행의 인덱스를 저장하는 리스트
    # 복원(Z 명령)을 위해 LIFO 방식으로 관리됨
    deleted = []

    # 각 행의 "위" 행을 가리키는 배열
    # 1번 인덱스부터 사용하며, up[i] = i 의 위쪽 행
    # 행은 처음부터 n개가 있으므로, up[1] = 0, up[2] = 1 ...
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+1)]

    # 현재 위치를 나타내는 인덱스 k
    k += 1

    # 주어진 명령어(cmd)를 하나씩 처리
    for cmd_i in cmd:
        # 현재 위치 삭제하고 그 다음위치로 이동
        if str(cmd_i).startswith("C"):
            # 현재 커서 위치 k를 삭제 스택에 저장
            deleted.append(k)


            up[down[k]] = up[k]
            down[up[k]] = down[k]

            # 커서 이동:
            # down[k] 이 테이블 범위를 벗어나면(up 방향으로 이동),
            # 그렇지 않으면 down 방향으로 이동
            k = up[k] if n<down[k] else down[k]

        # 가장 최근에 삭제한 행 복원
        elif str(cmd_i).startswith("Z"):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore

        # U 또는 D를 사용해 현재 위치를 위아래로 이동
        else:
            action, num = str(cmd_i).split()

            # U: 위로 이동 → up[] 배열 따라 이동
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            
            # D: 아래로 이동 → down[] 배열 따라 이동
            else:
                for _ in range(int(num)):
                    k = down[k]
    
    # 삭제된 행의 위치에 'X'를 그렇지 않은 행의 위치에 'O'를 포함하는 문자열 반환
    # 초기 상태는 모두 O (존재하는 행)
    answer = ["O"] * n

    # deleted 리스트에 남아 있는 인덱스는 실제로 삭제된 행
    # 내부에서 1-based 로 관리했으므로 -1 해줌
    for i in deleted:
        answer[i-1] = "X"

    # 리스트를 문자열로 결합하여 반환
    return "".join(answer)

n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
print(solution(n, k, cmd))