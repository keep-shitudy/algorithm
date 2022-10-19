# 2022.08.20
# 백준 / 14889번 스타트와 링크

from itertools import combinations

N = int(input())
S = []
answer = 0

for i in range(N):
    S.append(list(map(int, input().split(" "))))

teamCase = list(combinations(range(N), int(N/2)))

for i in range(int(len(teamCase)/2)):
    start = teamCase[i]
    link = teamCase[len(teamCase)-1-i]

    startCase = list(combinations(start, 2))
    linkCase = list(combinations(link, 2))

    startScore = 0
    linkScore = 0

    for sc in startCase:
        startScore += S[sc[0]][sc[1]]+S[sc[1]][sc[0]]

    for lc in linkCase:
        linkScore += S[lc[0]][lc[1]]+S[lc[1]][lc[0]]

    scoreDiff = abs(startScore-linkScore)
    if i == 0:
        answer = scoreDiff

    if answer > scoreDiff:
        answer = scoreDiff

print(answer)
