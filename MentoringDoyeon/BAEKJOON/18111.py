'''왜 안될까...'''
import sys

def work(height):
    time_count = 0
    for block in blocks_dict: #block은 높이 종류
        if block > height:
                time_count += (block - height) * 2 * blocks_dict[block]
        elif block < height:
                time_count += (height - block) * blocks_dict[block]
    return time_count

'''입력'''
N, M, B = map(int, sys.stdin.readline().split())
grid = []
for _ in range(N):
    grid.extend(map(int, sys.stdin.readline().split())) #extend는 여러개 입력
''''''
time_result, height_result = 128000000, 0

blocks = sum(grid) + B

blocks_dict = {}
for i in grid:
    if i not in blocks_dict.keys():
        blocks_dict[i] = grid.count(i)

for height in range(257): # 0~257 전부 탐색
    blocks_need = N * M * height
    if blocks >= blocks_need: # 가진블록이 필요한 블럭많을때만
        time_count = work(height)
        if time_count <= time_result:
            time_result = time_count
            height_result = height

print(time_result, height_result)