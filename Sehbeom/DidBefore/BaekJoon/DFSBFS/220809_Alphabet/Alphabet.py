# 22.08.09
# 백준 / 1987번 알파벳
# 시간초과로 인해 정답률이 많이 낮음. Pypy3로 해야 통과할 수 있음.

global answerMax
global case

answerMax = 0
case = ((0, -1), (0, 1), (1, 0),  (-1, 0))


def DFS(board, pos, visited, answer):
    global case
    global answerMax
    nextPos = []

    answer += 1
    visited[ord(board[pos[0]][pos[1]])-65] = True

    for i in case:
        nextPos.extend([pos[0]+i[0], pos[1]+i[1]])
        if (0 <= nextPos[0] < R) and (0 <= nextPos[1] < C):
            if not visited[ord(board[nextPos[0]][nextPos[1]])-65]:
                DFS(board, nextPos, visited, answer)
                visited[ord(board[nextPos[0]][nextPos[1]])-65] = False

        nextPos.clear()
    if answerMax < answer:
        answerMax = answer


R, C = map(int, input().split(" "))
board = []
for i in range(R):
    board.append(list(input()))

DFS(board, (0, 0), [False]*26, 0)
print(answerMax)
