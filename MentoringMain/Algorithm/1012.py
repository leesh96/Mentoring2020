import sys
sys.setrecursionlimit(10000)    # 재귀 호출 제한 설정(기본 값 = 1000 이상 해줘야 런타임 에러 x)

# 상하좌우 방향 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if land[nx][ny] == 1:
                land[nx][ny] = -1
                dfs(nx, ny)


t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    land = [[0]*m for _ in range(n)]
    bug_count = 0

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        land[y][x] = 1

    for i in range(n):
        for j in range(m):
            if land[i][j] > 0:
                dfs(i, j)
                bug_count += 1

    print(bug_count)
