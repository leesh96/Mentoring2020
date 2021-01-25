import sys
sys.setrecursionlimit(100000)

def divid(x, y, n):
    global white, blue

    if n <= 1:
        if map[x][y] == '0':
            white += 1
        elif map[x][y] == '1':
            blue += 1
        return
    for i in range(x, x + n):
        for j in range(y, y + n):
            if map[x][y] != map[i][j]:
                n = n//2
                divid(x, y, n) #1사분면
                divid(x + n, y, n) #2사분면
                divid(x, y + n, n) #3사분면
                divid(x+ n, y + n, n) #4사분면
                return
    if map[x][y] == '0':
        white += 1
        return
    elif map[x][y] == '1':
        blue += 1
        return


N = int(sys.stdin.readline())
map = []

for i in range(N):
    map.append(sys.stdin.readline().split())

white, blue = 0, 0
divid(0, 0, N)

print(white, blue, sep = "\n")