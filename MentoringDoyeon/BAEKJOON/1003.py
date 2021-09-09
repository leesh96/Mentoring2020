import sys
def fibo(n):
    fibo_memo = [[1, 0], [0, 1]]
    if n == 0:
        return fibo_memo[0]
    elif n == 1:
        return fibo_memo[1]
    else:
        i = 2
        while i <= n:
            fibo_memo.append([fibo_memo[i-1][0]+fibo_memo[i-2][0], fibo_memo[i-1][1]+fibo_memo[i-2][1]])
            i += 1
        return fibo_memo[n]

N = int(sys.stdin.readline())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline()))

for a in array:
    cnt0, cnt1 = fibo(a)
    print(cnt0, cnt1, sep=" ")
