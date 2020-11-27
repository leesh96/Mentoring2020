import sys

N, M, B = map(int, sys.stdin.readline().split())

input_list = [list(map(int,sys.stdin.readline().split())) for _ in range(N)] #좌표 이중리스트로 받음

grid = sum(input_list, []) #이중리스트 1차원리스트로

def work(grid, inventory, height): #목표 높이가 되도록 블럭 +-, inventory는 블럭개수.
    time_count = 0
    for block in grid:
        if block > height:
            time_count += (block - height) * 2
            inventory += (block - height)
        elif block < height:
            time_count += (height - block)
            inventory -= (height - block)
    return time_count, inventory

height_list = range(0, 256) #목표 높이
time_result, height_result= [], []


for height in height_list:
    time_count, inventory = work(grid, B, height)
    if inventory < 0: # 만약 인벤토리에 블럭이 음수이면 있을 수 없는 경우이므로 pass
        continue
    else:
        time_result.append(time_count)
        height_result.append(height)

#가능한 경우 중 시간 최솟값과 그때 높이 출력
print(min(time_result), height_result[time_result.index(min(time_result))])