# 22.09.23
# 백준 / 7562번 나이트의 이동

from collections import deque

# 내가 푼 코드
# board에 방문 여부를 T/F로 저장한 후, 계층을 나누어 해당 칸까지 이동한 횟수를 answer 변수에 저장함
# ex)
# 시작점 -> queue에 이동 가능한 8개 저장 : 1계층 -> answer = 1
# 1계층 좌표들 차례대로 popleft 되어 queue에 push : 2계층 -> answer = 2
# ...


def countRoute(board, size, initPos, destPos):
    queue = deque([initPos])
    oldOne = 1
    newOne = 0
    answer = 0

    while queue:
        pos = queue.popleft()
        oldOne -= 1

        for c in moveCase:
            x = pos[0] + c[0]
            y = pos[1] + c[1]
            if x < 0 or x >= size or y < 0 or y >= size:
                continue

            if not board[y][x]:
                if [x, y] == destPos:
                    answer += 1
                    return answer
                queue.append([x, y])
                board[y][x] = True
                newOne += 1
        if oldOne == 0:
            answer += 1
            oldOne = newOne
            newOne = 0


# 구글링으로 참고한 코드
# board에 방문 여부가 아닌 횟수를 저장함. (내가 푼 코드에서는 answer에 해당)
# board가 아직 방문되지 않으면(= 0 이면) 현재 popleft 되어진 좌표에 적힌 횟수 + 1 을 저장함
# 수행 시간에는 큰 차이가 없지만 좀 더 직관적이고 쉽게 풀 수 있는 방법인 것 같다.
def countRoute2(board, initPos, destPos):
    queue = deque([initPos])
    while queue:
        pos = queue.popleft()

        for c in moveCase:
            x = pos[0] + c[0]
            y = pos[1] + c[1]
            if x < 0 or x >= size or y < 0 or y >= size:
                continue
            if board[y][x] == 0:
                if [x, y] == destPos:
                    return board[pos[1]][pos[0]] + 1
                queue.append([x, y])
                board[y][x] = board[pos[1]][pos[0]] + 1


T = int(input())

moveCase = [(-1, -2), (1, -2), (-2, -1), (2, -1),
            (-2, 1), (2, 1), (-1, 2), (1, 2)]

for i in range(T):
    size = int(input())
    initPos = list(map(int, input().split()))
    destPos = list(map(int, input().split()))
    board = [[False] * size for i in range(size)]

    if initPos == destPos:
        print(0)
    else:
        # print(countRoute(board, size, initPos, destPos))
        print(countRoute2(board, initPos, destPos))
