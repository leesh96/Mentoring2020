import sys
#틀림

n, r, c = map(int, sys.stdin.readline().split())

def DAC(m, r, c):
    m = m // 2
    cnt = 0
    if m <= 1:
        if r == 1 and c == 1:
            cnt += 0
        elif r == 1 and c == 2:
            cnt += 1
        elif r == 2 and c == 1:
            cnt += 2
        else:
            cnt += 3
        return cnt
    if r > m and c > m: #4사분면
        cnt = cnt + (m * m * 3) + DAC(m, r//2, c//2)
        return cnt
    elif r > m and c <= m: #3사분면
        cnt = cnt + (m * m * 2) + DAC(m, r//2, c)
        return cnt
    elif r <= m and c > m: #2사분면
        cnt = cnt + (m * m * 1) + DAC(m, r, c//2)
        return cnt
    else:
        if r == 1 and c == 1:
            cnt += 0
        elif r == 1 and c == 2:
            cnt += 1
        elif r == 2 and c == 1:
            cnt += 2
        else:
            cnt += 3
        return cnt
    return cnt

M = 2 ** n #전체 셀 개수

print(DAC(M, r+1, c+1))