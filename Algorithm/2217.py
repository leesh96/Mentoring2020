import sys

N = int(sys.stdin.readline())
rope = list(int(sys.stdin.readline()) for _ in range(N))
rope.sort(reverse=True)

for i in range(N):
    rope[i] = rope[i] * (i + 1)

print(max(rope))
