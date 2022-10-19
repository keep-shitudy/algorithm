# 2022.10.05
# 백준 / 2293번 동전1

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

cases = [0] * (k+1)
cases[0] = 1

for c in coins:
    for i in range(1, k+1):
        if i < c:
            continue

        cases[i] += cases[i-c]

print(cases[k])
