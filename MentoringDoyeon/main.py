nm = input().split()
nm = list(map(int, nm))
chess = []
for i in range(nm[0]):
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
    return(abs(replace_num_B - replace_num_W)) #둘중 최소값 반환#

list_sample_num = []
for i in range(0, nm[0]-7):#nm[0] = 13일때 nm[0]-7=6 즉 range는 0~5 경우의 수 6개
    for j in range(0, nm[1]-7):
        list_sample = []
        for k in range(i, i+8):
            list_sample.append(chess[k][j:j+8])
        list_sample_num.append(Check(list_sample)) #받은 최소값을 리스트에 추가하면 모든 경우에 대한 최소값을 얻을 수 있다#

print(min(list_sample_num), end='')




# 2739
# num = int(input())
#
# for i in range(2, num+1):
#     for j in range(1, 10):
#         # print("{} * {} = {}".format(i, j, i * j))
#         print(i, '*', j, '=', i*j)
