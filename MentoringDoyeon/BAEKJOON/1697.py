import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

q = deque()
q.append(n)
visit = [0 for i in range(100001)]
visit[n] = 1
while q:
    i = q.popleft()

    if i == k:
        break

    if i-1 >= 0 and visit[i-1] == 0:
        visit[i-1] = visit[i] + 1
        q.append(i-1)
    if i+1 < 1000001 and visit[i+1] == 0:
        visit[i + 1] = visit[i] + 1
        q.append(i+1)
    if i*2 < 1000001 and visit[i*2] == 0:
        visit[i * 2] = visit[i] + 1
        q.append(i*2)

print(visit[k]-1)

