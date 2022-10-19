# 22.09.29
# 백준 / 10026번 적록색약

def checkArea(visited, pos, isWeak):
    stack = [pos]
    visited[pos[1]][pos[0]] = True

    while stack:
        curPos = stack.pop()
        for s in sameAreaCase:
            nextX = curPos[0] + s[0]
            nextY = curPos[1] + s[1]
            if nextX < 0 or nextX >= N or nextY < 0 or nextY >= N:
                continue

            visitedValue = visited[nextY][nextX]

            if not visitedValue:
                curValue = board[curPos[1]][curPos[0]]
                nextValue = board[nextY][nextX]
                if isWeak:
                    if (nextValue == curValue) or (
                        curValue == 'R' and nextValue == 'G') or (
                            curValue == 'G' and nextValue == 'R'):
                        stack.append([nextX, nextY])
                        visited[nextY][nextX] = True

                else:
                    if nextValue == curValue:
                        stack.append([nextX, nextY])
                        visited[nextY][nextX] = True


N = int(input())
board = []
for i in range(N):
    board.append(list(input()))

weakVisited = [[False] * N for i in range(N)]
notWeakVisited = [[False] * N for i in range(N)]

sameAreaCase = [[-1, 0], [1, 0], [0, -1], [0, 1]]
notWeakAns = 0
weakAns = 0

x = 0
y = 0
while x < N and y < N:
    while (y < N) and (weakVisited[y][x]):
        x += 1
        if x >= N:
            x = 0
            y += 1
    if y < N:
        weakAns += 1
        checkArea(weakVisited, [x, y], True)

x = 0
y = 0
while x < N and y < N:
    while (y < N) and (notWeakVisited[y][x]):
        x += 1
        if x >= N:
            x = 0
            y += 1
    if y < N:
        notWeakAns += 1
        checkArea(notWeakVisited, [x, y], False)

print(notWeakAns, weakAns)
