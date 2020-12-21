import sys
from collections import deque

x_direction = [1, -1, 0, 0]
y_direction = [0, 0, 1, -1]


def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    cnt = 1
    visited[x][y] = True

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            x_next = x + x_direction[i]
            y_next = y + y_direction[i]
            if (0 > x_next or x_next >= N) or (0 > y_next or y_next >= M):
                continue
            if path[x_next][y_next] and not visited[x_next][y_next]:
                Q.append((x_next, y_next))
                visited[x_next][y_next] = True
                cnt += 1
    return cnt


N, M, K = map(int, sys.stdin.readline().split())
path = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
result = 0

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    path[x - 1][y - 1] = 1

for i in range(N):
    for j in range(M):
        if path[i][j] and not visited[i][j]:
            result = max(result, bfs(i, j))

print(result)
