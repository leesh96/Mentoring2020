import sys
sys.setrecursionlimit(50000) #런타임에러나서..

def Test_f():
    def bfs(x, y):
        queue = []

        check_list = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(4):
            plus_x, plus_y = check_list[i]
            if x + plus_x < 0 or x + plus_x > M - 1 or y + plus_y < 0 or y + plus_y > N - 1:  # 좌표 넘어가면 X
                continue

            if grid[x + plus_x][y + plus_y] == 1:
                queue.append([x + plus_x, y + plus_y])
                grid[x + plus_x][y + plus_y] = 0
        for queue_x, queue_y in queue:
            grid[queue_x][queue_y] = 0
            bfs(queue_x, queue_y)



    def dfs(x, y):
        check_list = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 탐색할때 더하고뺄 좌표
        for i in range(4):  # 상하좌우 4번 반복
            plus_x, plus_y = check_list[i]
            if x + plus_x < 0 or x + plus_x > M - 1 or y + plus_y < 0 or y + plus_y > N - 1:  # 좌표 넘어가면 X
                continue
            if grid[x + plus_x][y + plus_y] == 1:  # 탐색한 좌표 값이 1이면 0으로 바꾸고(다시탐색X) 다시 그 좌표에 대해 check
                grid[x + plus_x][y + plus_y] = 0
                dfs(x + plus_x, y + plus_y)

    ###입력
    M, N, K = map(int, sys.stdin.readline().split())
    grid = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = (list(map(int, sys.stdin.readline().split())))
        grid[x][y] = 1
    ###

    earthworm = 0

    for x in range(M):
        for y in range(N):
            if grid[x][y] == 1:
                bfs(x, y)
                earthworm += 1 #상하좌우 전부 0이면 check 반복 끝. 지렁이 += 1
    print(earthworm)

Test = int(sys.stdin.readline())

for _ in range(Test): # 테스트 수 만큼 반복
    Test_f()
