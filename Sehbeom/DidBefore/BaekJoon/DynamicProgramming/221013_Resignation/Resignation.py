# 2022.10.13
# 백준 / 14501번 퇴사

N = int(input())
T = [0]
P = [0]

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

maxAdvantage = [0]*(N+1)

for i in range(1, N+1):
    todayMax = 0
    if T[i] > 1:
        todayMax = maxAdvantage[i-1]
        if (i + T[i] - 1) <= N:
            if maxAdvantage[i + T[i] - 1] < (todayMax + P[i]):
                maxAdvantage[i + T[i] - 1] = todayMax + P[i]

    else:
        todayMax = maxAdvantage[i-1] + P[i]

    maxAdvantage[i] = max(todayMax, maxAdvantage[i])

print(maxAdvantage[N])
