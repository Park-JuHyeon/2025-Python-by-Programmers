# 문제07 방문길이 복습
# 여러개 솔루션 활용 풀이

def check_place(nx, ny):
    return 0<=nx<=10 and 0<=ny<=10

def update_place(x, y, dir):
    if dir == 'U':
        nx, ny = x, y+1
    elif dir == 'D':
        nx, ny = x, y-1
    elif dir == 'R':
        nx, ny = x+1, y
    elif dir == 'L':
        nx, ny = x-1, y
    return nx, ny

def solution(dirs):
    x, y = 5, 5
    ans = set()

    for dir in dirs:
        nx, ny = update_place(x, y, dir)

        if not check_place(nx, ny):
            continue
        ans.add((nx,ny,x,y))
        ans.add((x,y,nx,ny))
        x, y = nx, ny
    result = len(ans)/2

    return result

dirs = 'LULLLLLLU'
print(solution(dirs))