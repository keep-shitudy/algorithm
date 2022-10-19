# 2022.08.23
# 백준 / 2798번 블랙잭

from itertools import combinations

N, M = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))

answer = 0
isFirst = True

cases = list(combinations(cards, 3))

for c in cases:
    if sum(c) > M:
        continue

    else:
        if isFirst:
            isFirst = False
            answer = sum(c)
            continue

        if answer < sum(c):
            answer = sum(c)

print(answer)
