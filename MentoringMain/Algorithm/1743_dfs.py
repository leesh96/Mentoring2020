import sys
sys.setrecursionlimit(10000)

x_direction = [1, -1, 0, 0]
y_direction = [0, 0, 1, -1]


def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1

    for i in range(4):
        x_next = x + x_direction[i]
        y_next = y + y_direction[i]
        if (0 <= x_next < N) and (0 <= y_next < M):
            if path[x_next][y_next] == 1 and not visited[x_next][y_next]:
                dfs(x_next, y_next)


N, M, K = map(int, sys.stdin.readline().split())
path = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
result = 0

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    path[x - 1][y - 1] = 1

for i in range(N):
    for j in range(M):
        if path[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            result = max(result, cnt)

print(result)
