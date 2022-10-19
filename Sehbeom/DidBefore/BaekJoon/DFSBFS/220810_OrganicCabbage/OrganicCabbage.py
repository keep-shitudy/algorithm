# 22.08.10
# 백준 / 1012번 유기농 배추
# 재귀로 풀었을 때는 재귀가 너무 깊어 런타임 에러가 발생
# -> 스택으로 다시 풀어서 성공!

# <재귀 활용 코드>
# def DFS(ground, pos, cabbagePos):
#     ground[pos[1]][pos[0]] = False
#     cabbagePos[(pos[0], pos[1])] = False

#     for i in case:
#         nextX = pos[0]+i[0]
#         nextY = pos[1]+i[1]
#         if 0 <= nextX < M and 0 <= nextY < N:
#             if ground[nextY][nextX]:
#                 DFS(ground, [nextX, nextY], cabbagePos)

# <스택 활용 코드>
def DFS(ground, pos, cabbagePos):
    stack = []
    stack.append((pos[0], pos[1]))

    while stack:
        curPos = stack.pop()
        ground[curPos[1]][curPos[0]] = False
        cabbagePos[(curPos[0], curPos[1])] = False
        for i in case:
            nextX = curPos[0]+i[0]
            nextY = curPos[1]+i[1]
            if 0 <= nextX < M and 0 <= nextY < N:
                if ground[nextY][nextX]:
                    stack.append((nextX, nextY))


T = int(input())
answer = [0]*T
case = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(T):
    M, N, K = map(int, input().split(" "))
    ground = [[False]*M for i in range(N)]
    cabbagePos = {}

    for j in range(K):
        X, Y = map(int, input().split(" "))
        ground[Y][X] = True
        cabbagePos[(X, Y)] = True

    for c in cabbagePos:
        if cabbagePos[c]:
            answer[i] += 1
            DFS(ground, c, cabbagePos)

for a in answer:
    print(a)
