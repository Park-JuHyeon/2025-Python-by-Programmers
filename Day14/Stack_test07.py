# 스택 문제 14 표 편집 (고난이도) p177
# 명령어 기반 표의 행을 선택, 삭제, 복구하는 프로그램 작성
# "U X" : 현재 선택한 행에서 X칸 위에 있는 행 선택
# "D X" : 현재 선택한 행에서 X칸 아래에 있는 행 선택
# "C" : 현재 선택한 행을 삭제한 후, 바로 아래 행을 선택 (단 삭제된 행이 가장 마지막 행인 경우 바로 윗행 선택)
# "Z" : 가장 최근에 삭제한 행을 원래대로 복구 (단 현재 선택한 행은 바뀌지 않습니다.)

# 처음 표의 행 개수를 나타내는 정수 n, 처음 선택한 행의 위치 정수 k
# 수행한 명령어가 담긴 문자열 배열 cmd 주어질때
# 모든 명령어 수행 후 표의 상태와 처음 표의 상태 비교, 삭제되지 않은 행 "O", 삭제된 행 "X" 반환

def move_Down():
    
    return

def move_Up():

    return

def delete_Line():

    return

def return_Line():

    return

def solution(n, k, cmd):


    return

n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
print(solution(n, k, cmd))