# 2022.08.
# 프로그래머스 lv1 / 키패드 누르기

# 나의 풀이
def solution(numbers, hand):
    answer = []
    positionInfo = {0: (1, 3, 'O')}
    currentPos = {'L': (0, 3), 'R': (2, 3)}
    for i in range(0, 9):
        positionInfo[i+1] = (i % 3, int(i/3), chr(76+3*(i % 3)))

    for n in numbers:
        if positionInfo[n][2] == 'O':
            distanceL = abs(currentPos['L'][0]-positionInfo[n][0]) + \
                abs(currentPos['L'][1]-positionInfo[n][1])
            distanceR = abs(currentPos['R'][0]-positionInfo[n][0]) + \
                abs(currentPos['R'][1]-positionInfo[n][1])

            if distanceL == distanceR:
                answer.append(hand[0].upper())
                currentPos[hand[0].upper()] = positionInfo[n][0:2]
            else:
                ansHand = 'L' if distanceL < distanceR else 'R'
                answer.append(ansHand)
                currentPos[ansHand] = positionInfo[n][0:2]

        else:
            answer.append(positionInfo[n][2])
            currentPos[positionInfo[n][2]] = positionInfo[n][0:2]

    return ''.join(answer)

# 다른 사람 풀이 활용


def solution2(numbers, hand):
    answer = ''
    key_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    left = [1, 4, 7]
    right = [3, 6, 9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer


# 입출력 예
numbers_input1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand_input1 = "right"
# "LRLLLRLLRRL"

numbers_input2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand_input2 = "left"
# "LRLLRRLLLRR"

numbers_input3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand_input3 = "right"
# "LLRLLRLLRL"

print(solution(numbers_input1, hand_input1))
