# 2022.10.13
# 백준 / 9461번 파도반 수열

T = int(input())
padovanSeq = [0]*101
padovanSeq[1] = 1
padovanSeq[2] = 1
prevN = 3

for t in range(T):
    N = int(input())

    if N >= 3:
        for i in range(prevN, N+1):
            padovanSeq[i] = padovanSeq[i-2] + padovanSeq[i-3]

    if prevN < N:
        prevN = N

    print(padovanSeq[N])
