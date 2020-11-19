import sys

SIZE = 8
EVEN = True
ODD = False

'''
case1
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
짝수, 짝수 or 홀수, 홀수 B
else W

case2
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
짝수, 짝수 or 홀수, 홀수 W '''


def check_chess(chess):

    case1 = 0  # input_chess[0][0] = Black
    for row in range(SIZE):
        for col in range(SIZE):
            chkrow = (EVEN if row % 2 == 0 else ODD)
            chkcol = (EVEN if col % 2 == 0 else ODD)
            if (chkrow == EVEN and chkcol == EVEN) or (chkrow == ODD and chkcol == ODD):
                if chess[row][col] != 'B':
                    case1 += 1
            if (chkrow == EVEN and chkcol == ODD) or (chkrow == ODD and chkcol == EVEN):
                if chess[row][col] != 'W':
                    case1 += 1

    case2 = 0  # input_chess[0][0] = White
    for row in range(SIZE):
        for col in range(SIZE):
            chkrow = (EVEN if row % 2 == 0 else ODD)
            chkcol = (EVEN if col % 2 == 0 else ODD)
            if (chkrow == EVEN and chkcol == EVEN) or (chkrow == ODD and chkcol == ODD):
                if chess[row][col] != 'W':
                    case2 += 1
            if (chkrow == EVEN and chkcol == ODD) or (chkrow == ODD and chkcol == EVEN):
                if chess[row][col] != 'B':
                    case2 += 1

    result.append(min(case1, case2))


N, M = map(int, sys.stdin.readline().split())
input_chess = [list(sys.stdin.readline()) for _ in range(N)]
result = []

for i in range(N - 7):
    for j in range(M - 7):
        copy_chess = [input_chess[i + x][j:j + SIZE] for x in range(SIZE)]
        check_chess(copy_chess)

print(min(result))
