# 교재 129p 문제 07 방문길이 복습
# 솔루션하나로 구현

def solution(dirs):
    x, y = 0, 0
    ans = set()
    dir = {'U':(0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}

    for i in dirs:
        nx, ny = x + dir[i][0], y + dir[i][1]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            ans.add((x,y,nx,ny))
            ans.add((nx,ny,x,y))
            x, y = nx, ny

    return len(ans)/2

dirs = "ULURRDLLU"
print(solution(dirs))




