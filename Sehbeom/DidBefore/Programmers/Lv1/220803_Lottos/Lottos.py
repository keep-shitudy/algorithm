# 2022.08.03
# 프로그래머스 lv1 / 로또의 최고 순위와 최저 순위

# 나의 풀이
def solution(lottos, win_nums):
    answer = [0]*2
    equalResult = [0]*2

    for l in lottos:
        if l == 0:
            equalResult[0] += 1
        elif l in win_nums:
            equalResult[0] += 1
            equalResult[1] += 1

    for i in range(0, 2):
        if equalResult[i] <= 1:
            answer[i] = 6
        else:
            answer[i] = 7-equalResult[i]

    return answer

# 다른 사람 풀이 활용


def solution2(lottos, win_nums):
    answer = [0]*2
    equalResult = [0]*2

    rankInfo = [6, 6, 5, 4, 3, 2, 1]

    for l in lottos:
        if l == 0:
            equalResult[0] += 1
        elif l in win_nums:
            equalResult[0] += 1
            equalResult[1] += 1

    answer[0] = rankInfo[equalResult[0]]
    answer[1] = rankInfo[equalResult[1]]

    return answer


# 입출력 예
lottos_input1 = [44, 1, 0, 0, 31, 25]
win_nums_input1 = [31, 10, 45, 1, 6, 19]
# [3, 5]

lottos_input2 = [0, 0, 0, 0, 0, 0]
win_nums_input2 = [38, 19, 20, 40, 15, 25]
# [1, 6]

lottos_input3 = [45, 4, 35, 20, 3, 9]
win_nums_input3 = [20, 9, 3, 45, 4, 35]
# [1, 1]

print(solution2(lottos_input3, win_nums_input3))
