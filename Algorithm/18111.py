import sys


def count_sec(h):
    sec = 0
    """
    작업1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. -> 2초 고르려는 높이 < 현재 높이일 때
    작업2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. -> 1초 고르려는 높이 > 현재 높이일 때
    """
    for key in base_info:   # 입력된 베이스에 존재하는 높이에 대해서만 작업
        if key > h:    # 작업 1
            sec += 2 * (key - h) * base_info[key]      # 제거할 블록 수 * 해당 높이를 가진 블록 수 * 2초
        elif key < h:  # 작업 2
            sec += (h - key) * base_info[key]          # 놓을 블록 수 * 해당 높이를 가진 블록 수

    return sec      # 결국 전체 판을 고르는데 걸리는 시간 저장


# 입력
N, M, B = map(int, sys.stdin.readline().split())
base = []
for _ in range(N):
    base.extend(map(int, sys.stdin.readline().split()))

# 존재하는 높이, 해당 높이 몇 칸씩 존재 카운트?
base_info = {}      # 키 = 존재하는 높이, value = 칸 수
for i in base:
    if i not in base_info.keys():
        base_info[i] = base.count(i)

land_size = N * M
has_block = sum(base) + B   # 가지고 있는 블럭 = 현재 땅의 상태 + 인벤토리
target_sec = 128000000      # 최소 시간, 초기값은 500*500*256 크기의 땅을 0 높이로 고르는데 걸리는 시간
target_height = 0           # 목표 높이

# 높이 0 ~ 256에 대해 완전탐색
for height in range(257):
    need_block = height * land_size     # 필요한 블럭 = 고르려는 높이 * 땅의 크기
    if need_block <= has_block:         # 필요한 블럭 <= 가지고 있는 블럭 일 때만 그 높이로 고를 수 있음
        tmp_sec = count_sec(height)
        if tmp_sec <= target_sec:       # height 높이로 고르는데 걸리는 시간이 최소 시간보다 작으면
            target_height = height      # 높이와 시간 교체
            target_sec = tmp_sec

print(target_sec, target_height)
