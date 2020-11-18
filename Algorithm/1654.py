import sys

K, N = map(int, sys.stdin.readline().split())
lan_has = []

for i in range(K):
    lan_has.append(int(sys.stdin.readline()))

start = 0
end = max(lan_has)

while start <= end:
    middle = (start + end) // 2
    lan_cutting = 0
    for lan in lan_has:
        lan_cutting += lan // middle

    if lan_cutting >= N:
        start = middle + 1
    else:
        end = middle - 1

print(end)
