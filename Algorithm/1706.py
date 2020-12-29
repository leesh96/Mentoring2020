import sys

# 입력
R, C = map(int, sys.stdin.readline().split())
crossword = [list(sys.stdin.readline()) for _ in range(R)]
result = []

# 가로 단어 찾기
for i in range(R):
    temp = ""
    for j in range(C):
        if crossword[i][j] != '#':
            temp += crossword[i][j]
        if crossword[i][j] == '#' or j == C - 1:
            if len(temp) > 1:
                result.append(temp)
                temp = ""
            else:
                temp = ""


# 세로 단어 찾기
for i in range(C):
    temp = ""
    for j in range(R):
        if crossword[j][i] != '#':
            temp += crossword[j][i]
        if crossword[j][i] == '#' or j == R - 1:
            if len(temp) > 1:
                result.append(temp)
                temp = ""
            else:
                temp = ""


# 결과
result.sort()
print(result[0])
