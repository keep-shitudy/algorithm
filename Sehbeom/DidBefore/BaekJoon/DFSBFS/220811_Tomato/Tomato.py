# 22.08.11
# 백준 / 7576번 토마토

from collections import deque


def BFS(box, queue):
    newQueue = deque()
    while queue:
        curPos = queue.popleft()

        for c in case:
            nextPos = (curPos[0]+c[0], curPos[1]+c[1])
            if 0 <= nextPos[0] < M and 0 <= nextPos[1] < N:
                if box[nextPos[1]][nextPos[0]] == 0:
                    box[nextPos[1]][nextPos[0]] = 1
                    newQueue.append(nextPos)

    return newQueue


case = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

M, N = map(int, input().split(" "))

box = [[0]*M for i in range(N)]
firstRipen = []
isAllOne = True

for i in range(N):
    b = list(map(int, input().split(" ")))
    if 1 in b:
        for j in range(len(b)):
            box[i][j] = b[j]
            if b[j] == 1:
                firstRipen.append((j, i))
            elif b[j] == 0:
                isAllOne = False
        continue

    isAllOne = False
    box[i] = b

if isAllOne:
    print(0)
    exit()
else:
    queue = deque(firstRipen)
    notAllRipen = False

    while queue:
        queue = BFS(box, queue)
        answer += 1

    for i in box:
        if 0 in i:
            notAllRipen = True
            answer = 0

    print(answer-1)
