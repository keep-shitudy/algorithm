# 2022.08.23
# 백준 / 9663번 N-Queens

import time


def printBoard(board):
    for i in range(1, len(board)):
        print(board[i], end=" ")
        if i % N == 0:
            print("\n")


def checkQueensRoute(board, pos):
    board[pos] = False

    horizonStart = pos - ((pos % N)-1) if not (pos % N == 0) else pos-N+1
    verticalStart = pos % N if (pos % N != 0) else N
    for i in range(N):
        board[horizonStart+i] = False
        board[verticalStart+i*N] = False

    temp = pos
    while (temp > N) and (temp % N != 1):
        temp -= (N+1)
        board[temp] = False

    temp = pos
    while (temp < (N*N-N+1)) and (temp % N != 0):
        temp += (N+1)
        board[temp] = False

    temp = pos
    while (temp < (N*N-N+1)) and (temp % N != 1):
        temp += (N-1)
        board[temp] = False

    temp = pos
    while (temp > N) and (temp % N != 1):
        temp -= (N-1)
        board[temp] = False


def putQueens(board, startPos):
    global answer
    for i in range(startPos, startPos+N):
        curBoard = board[:]
        if curBoard[i]:
            checkQueensRoute(curBoard, i)

            if (startPos + N) == (N*N + 1):
                answer += 1
                break

            else:
                if True in curBoard[startPos+N:startPos+2*N]:
                    putQueens(curBoard, startPos + N)


def canPutQueens(curStack, curPos):
    if not curStack:
        return True
    else:
        stack = curStack[:]
        isPossible = True
        horizonStart = curPos - ((curPos % N) - 1) if not (curPos %
                                                           N == 0) else curPos - N + 1
        while stack:
            s = stack.pop()
            if s % N == curPos % N:
                isPossible = False
                break

            diag_rb = s
            diag_lb = s

            while True:
                if diag_rb % N != 0:
                    diag_rb += (N+1)

                if diag_lb % N != 1:
                    diag_lb += (N-1)

                if (diag_rb == curPos) or (diag_lb == curPos):
                    isPossible = False
                    break

                if (horizonStart <= diag_rb < horizonStart + N) or (horizonStart <= diag_lb < horizonStart + N):
                    break

                if (diag_rb % N == 0) and (diag_lb % N == 1):
                    break

        return isPossible


def putQueens3(stack, startPos):
    global answer

    for i in range(startPos, startPos+N):
        if canPutQueens(stack, i):
            stack.append(i)

            if (startPos + N) == (N*N + 1):
                answer += 1
                stack.pop()
                break

            else:
                putQueens3(stack, startPos + N)
                stack.pop()


def putQueens4(stack, startPos):
    global answer

    for i in range(startPos, startPos+N):
        isPossible = True
        if not stack:
            isPossible = True
        else:
            curStack = stack[:]
            horizonStart = i - ((i % N) - 1) if not (i % N == 0) else i - N + 1

            while curStack:
                s = curStack.pop()

                if s % N == i % N:
                    isPossible = False
                    break

                diag_rb = s
                diag_lb = s

                while True:
                    if diag_rb % N != 0:
                        diag_rb += (N+1)

                    if diag_lb % N != 1:
                        diag_lb += (N-1)

                    if (diag_rb == i) or (diag_lb == i):
                        isPossible = False
                        break

                    if (horizonStart <= diag_rb < horizonStart + N) or (horizonStart <= diag_lb < horizonStart + N):
                        break

                    if (diag_rb % N == 0) and (diag_lb % N == 1):
                        break

        if isPossible:
            stack.append(i)

            if (startPos + N) == (N*N + 1):
                answer += 1
                stack.pop()
                break

            else:
                putQueens4(stack, startPos + N)
                stack.pop()


def putQueens2(board, startPos):
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
                    putQueens2(curBoard, startPos + N)


N = int(input())
startTime = time.time()
board = [True for i in range(N*N + 1)]

answer = 0
putQueens4([], 1)
# putQueens2(board, 1)
# print(canPutQueens([1, 8, 15, 17], 21))
print(answer)
print("time : ", time.time() - startTime)
