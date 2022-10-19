# 2022.09.22
# 백준 / 1080번 행렬

N, M = map(int, input().split())

matrixA = []
matrixB = []
for i in range(N):
    matrixA.append(list(map(int, list(input()))))
for i in range(N):
    matrixB.append(list(map(int, list(input()))))

if N < 3 or M < 3:
    if matrixA == matrixB:
        print(0)
    else:
        print(-1)

else:
    x = 0
    y = 0
    answer = 0
    while y < (N-2):
        if x < (M-2):
            if matrixA[y][x] != matrixB[y][x]:
                answer += 1
                for i in range(y, y+3):
                    for j in range(x, x+3):
                        matrixA[i][j] = (matrixA[i][j]+1) % 2
            x += 1

        else:
            if matrixA[y] == matrixB[y]:
                x = 0
                y += 1
            else:
                print(-1)
                exit()

    if matrixA == matrixB:
        print(answer)
    else:
        print(-1)
