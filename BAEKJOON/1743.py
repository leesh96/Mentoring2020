import sys
sys.setrecursionlimit(50000)

def BFS(x, y):
    global cnt
    queue = []
    check = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for p_x, p_y in check:
        if x + p_x < 0 or x + p_x >= M or y + p_y < 0 or y + p_y >= N:
            continue
        if grid[x + p_x][y + p_y] == 1:
            grid[x + p_x][y + p_y] = 0
            queue.append([x + p_x, y + p_y])
            cnt += 1
    for c_x, c_y in queue:
        BFS(c_x, c_y)
    return cnt


N, M, K = map(int, sys.stdin.readline().split())

grid = [[0]*N for _ in range(M)]

for _ in range(K):
    y, x = map(int, sys.stdin.readline().split())
    y -= 1
    x -= 1
    grid[x][y] = 1

result = []
for x in range(M):
    for y in range(N):
        cnt = 0
        if grid[x][y] == 1:
            cnt += 1
            grid[x][y] = 0
            result.append(BFS(x, y))

print(max(result))

