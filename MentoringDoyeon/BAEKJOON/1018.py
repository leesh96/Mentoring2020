import sys

n, m = map(int, sys.stdin.readline().split())
chess = []
for i in range(n):
    chess.append(input())

def Check(chess):
    row = 8
    col = 8
    replace_num_W = 0
    replace_num_B = 0
    '''WB로 시작할때'''
    if chess[0][0] == 'W':
        for i in range(0, row, 2):
            for j in range(0, col, 2):
                if chess[i][j] == 'B':
                    replace_num_W += 1
        for i in range(1, row, 2):
            for j in range(1, col, 2):
                if chess[i][j] == 'B':
                    replace_num_W += 1
        for i in range(1, row, 2):
            for j in range(0, col, 2):
                if chess[i][j] == 'W':
                    replace_num_W += 1
        for i in range(0, row, 2):
            for j in range(1, col, 2):
                if chess[i][j] == 'W':
                    replace_num_W += 1
        '''BW로 시작할때'''
    elif chess[0][0] == 'B':
        for i in range(0, row, 2):
            for j in range(0, col, 2):
                if chess[i][j] == 'W':
                    replace_num_W += 1
        for i in range(1, row, 2):
            for j in range(1, col, 2):
                if chess[i][j] == 'W':
                    replace_num_W += 1
        for i in range(1, row, 2):
            for j in range(0, col, 2):
                if chess[i][j] == 'B':
                    replace_num_W += 1
        for i in range(0, row, 2):
            for j in range(1, col, 2):
                if chess[i][j] == 'B':
                    replace_num_W += 1
    return(abs(replace_num_B - replace_num_W))

list_sample_num = []
for i in range(0, n-7):
    for j in range(0, m-7):
        list_sample = []
        for k in range(i, i+8):
            list_sample.append(chess[k][j:j+8])
        list_sample_num.append(Check(list_sample))

print(min(list_sample_num))