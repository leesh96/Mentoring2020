import sys
from collections import deque
sys.setrecursionlimit(1000000)

def BFS(x, y):
    global cnt
    cnt = 1
    queue = deque()
    check = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue.append([x, y])

    while queue:
        c_x, c_y = queue.popleft()
        for p_x, p_y in check:
            if 0 <= c_x + p_x < M and 0 <= c_y + p_y < N:
                if grid[c_x + p_x][c_y + p_y] == 1 and [c_x + p_x, c_y + p_y] not in visit:
                    visit.append([c_x + p_x, c_y + p_y])
                    queue.append([c_x + p_x, c_y + p_y])
                    cnt += 1
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
    grid[x-1][y-1] = 1

result = []
visit = []

for x in range(M):
    for y in range(N):
        cnt = 0
        if grid[x][y] == 1:
            visit.append([x, y])
            result.append(BFS(x, y))

print(max(result))