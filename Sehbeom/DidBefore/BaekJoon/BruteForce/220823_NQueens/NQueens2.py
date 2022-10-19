def putQueens(board, startPos):
    global answer
    for i in range(startPos, startPos+N):
        curBoard = board[:]
        if curBoard[i]:
            curBoard[i] = False

            horizonStart = i - ((i % N)-1) if not (i % N == 0) else i-N+1
            verticalStart = i % N if (i % N != 0) else N

            for j in range(N):
                curBoard[horizonStart+j] = False
                curBoard[verticalStart+j*N] = False

            temp = i
            while (temp > N) and (temp % N != 1):
                temp -= (N+1)
                curBoard[temp] = False

            temp = i
            while (temp < (N*N-N+1)) and (temp % N != 0):
                temp += (N+1)
                curBoard[temp] = False

            temp = i
            while (temp < (N*N-N+1)) and (temp % N != 1):
                temp += (N-1)
                curBoard[temp] = False

            temp = i
            while (temp > N) and (temp % N != 1):
                temp -= (N-1)
                curBoard[temp] = False

            if (startPos + N) == (N*N + 1):
                answer += 1
                break

            else:
                if True in curBoard[startPos+N:startPos+2*N]:
                    putQueens(curBoard, startPos + N)


N = int(input())
board = [True for i in range(N*N + 1)]

answer = 0
putQueens(board, 1)
print(answer)
