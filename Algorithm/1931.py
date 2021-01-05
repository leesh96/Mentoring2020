import sys

# 입력
N = int(sys.stdin.readline())
conf = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
conf.sort(key=lambda x: (x[0], x[1]))
# conf.sort(key=lambda x: x[1])

# 회의실 배정 (종료시간이 빠른 순서대로) 그리디 알고리즘
last_end = 0
cnt = 0

for start, end in conf:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)
