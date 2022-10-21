# 2022.10.21
# 백준 / 2573 빙산
# Pypy3 로 통과

def passOneYear(pos):
    meltingAmount = []
    stack = [pos]
    visited[pos[0]][pos[1]] = True
    while stack:
        curPos = stack.pop()
        melting = 0

        for n in neerCase:
            nextX = curPos[1] + n[1]
            nextY = curPos[0] + n[0]

            if nextX < 0 or nextX >= M or nextY < 0 or nextY >= N:
                continue

            if iceberg[nextY][nextX] == 0:
                melting += 1

            else:
                if not visited[nextY][nextX]:
                    visited[nextY][nextX] = True
                    stack.append([nextY, nextX])
        if melting == 4:
            return
        meltingAmount.append([curPos[0], curPos[1], melting])

    for m in meltingAmount:
        iceberg[m[0]][m[1]] = iceberg[m[0]][m[1]] - \
            m[2] if iceberg[m[0]][m[1]] >= m[2] else 0


N, M = map(int, input().split())

iceberg = []
for i in range(N):
    inputList = list(map(int, input().split()))
    iceberg.append(inputList)

neerCase = [[0, -1], [0, 1], [-1, 0], [1, 0]]
answer = -1

icebergCount = 0
while icebergCount <= 1:
    visited = [[False]*M for i in range(N)]
    icebergCount = 0

    for i in range(N):
        for j in range(M):
            if (iceberg[i][j] != 0) and (not visited[i][j]):
                icebergCount += 1
                if icebergCount == 1:
                    answer += 1
                else:
                    print(answer)
                    exit()
                passOneYear([i, j])
    if icebergCount == 0:
        print(0)
        break
