import sys
sys.setrecursionlimit(50000)

def BFS(x, y):
    global cnt
    queue = []
    check = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for p_x, p_y in check:
        if 0 <= x + p_x < M and 0 <= y + p_y < N:
            if grid[x + p_x][y + p_y] == 1 and [x + p_x, y + p_y] not in visit:
                visit.append([x + p_x, y + p_y])
                queue.append([x + p_x, y + p_y])
                cnt += 1
    for c_x, c_y in queue:
        BFS(c_x, c_y)
    return cnt

def DFS(x, y):
    global cnt
    check = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for p_x, p_y in check:
        if 0 <= x + p_x < M and 0 <= y + p_y < N:
            if grid[x + p_x][y + p_y] == 1 and [x + p_x, y + p_y] not in visit:
                    visit.append([x + p_x, y + p_y])
                    cnt += 1
                    DFS(x + p_x, y + p_y)
    return cnt


N, M, K = map(int, sys.stdin.readline().split())

grid = [[0]*N for _ in range(M)]

for _ in range(K):
    y, x = map(int, sys.stdin.readline().split())
    y -= 1 #시작좌표가 1, 1이니까 1씩 빼준다    x -= 1
    grid[x][y] = 1

result = []
visit = []
queue = []

for x in range(M):
    for y in range(N):
        cnt = 0
        if grid[x][y] == 1:
            cnt += 1
            visit.append([x, y])
            result.append(BFS(x, y))

print(max(result))