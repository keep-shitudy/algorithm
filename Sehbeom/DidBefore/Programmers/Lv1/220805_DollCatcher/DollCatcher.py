# 2022.08.05
# 프로그래머스 lv1 / 크레인 인형뽑기 게임

# 나의 풀이
def solution(board, moves):
    answer = 0
    bucket = []

    for m in moves:
        i = 0
        while i < len(board)-1 and board[i][m-1] == 0:
            i += 1
        if board[i][m-1] == 0:
            continue

        bucket.append(board[i][m-1])
        board[i][m-1] = 0

        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            bucket.pop()
            bucket.pop()
            answer += 2

    return answer

# 다른 사람 풀이 활용


def solution2(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a


# 입출력 예
board_input1 = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves_input1 = [1, 5, 3, 5, 1, 2, 1, 4]
# 4

print(solution2(board_input1, moves_input1))
