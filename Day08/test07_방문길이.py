# 문제 07 방문길이
# 캐릭터는 (0,0) 에서 시작, 좌표평면은 왼쪽 위 (-5,5), 아래 (-5,-5), 오른쪽 위 (5,5), 아래 (5,-5)로 구성

# 게임 캐릭터가 지나간 길 중, 캐릭터가 처음 걸어본 길의 길이를 구한다.
#   - 이미 거쳐간 길은 길이에서 제외, 좌표평면 넘어가면 무시

# 명령어가 매개변수 dirs로 주어질때, 캐릭터가 처음 걸어본 길의 길이구하는 solution() 완성

# 음수좌표를 2차원 배열에서 사용할수 없으므로 원점을 (0,0) -> (5,5)로 변경한다
def is_valid_move(nx, ny):
    return 0<=nx<11 and 0<=ny<11

# 각 입력 방향키 별 x,y 좌표 변경 함수
def update_location(x, y, dir):
    if dir == 'U':
        nx, ny = x, y+1
    elif dir == 'D':
        nx, ny = x, y-1
    elif dir == 'L':
        nx, ny = x-1, y
    elif dir == 'R':
        nx, ny = x+1, y
    
    return nx, ny

def solution(dirs):
    # 원점 (5,5)로 변경
    x, y = 5,5
    # 자동 중복제거 set() 함수 - (한번 가본길은 카운트하지 않는다.)
    ans = set()

    # 문자열 dirs를 문자 하나씩 순회
    for dir in dirs:
        # 명령어 별 이동한 x,y 좌표 업데이트
        nx, ny = update_location(x, y, dir)
        # 이동좌표가 0 이상 11 미만인지 확인, 넘어가면 다음 문자 실행
        if not is_valid_move(nx, ny):
            continue
        # A -> B 로 간 경우에는 반대인 B -> A도 추가해야함 (같은경우이므로 추후 나눠줘야함)
        ans.add((x,y,nx,ny))
        ans.add((nx,ny,x,y))
        # x,y 좌표 이동한 좌표로 업데이트
        x , y = nx, ny

    # 반대인 경우도 추가했으므로 2로 나눠줘야함
    return len(ans)/2

dirs = "LULLLLLLU"
print(solution(dirs))


