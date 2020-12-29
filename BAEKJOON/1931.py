import sys

#입력
N = int(sys.stdin.readline())
array = []

for _ in range(N):
    array.append(tuple(map(int, sys.stdin.readline().split())))

array.sort(key=lambda x: (x[1], x[0])) #끝나는시간으로 한번, 시작하는 시간으로 한번 정렬

cnt = 0
endtime = 0
for i in range(N):
    if array[i][0] >= endtime: #끝나는시간이 시작하는시간보다 크면 회의가능
        endtime = array[i][1]
        cnt += 1

print(cnt)

