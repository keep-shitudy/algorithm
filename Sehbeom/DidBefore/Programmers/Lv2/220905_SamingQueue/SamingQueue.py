# 2022.09.05
# 프로그래머스 lv2 / 두 큐 합 같게 만들기

# 나의 풀이
from collections import deque


def solution(queue1, queue2):
    answer = 0

    len_q1 = len(queue1)
    len_q2 = len(queue2)

    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)

    q1 = deque(queue1)
    q2 = deque(queue2)

    while len_q1 >= 0 or len_q2 >= 0:
        if sum_q1 == sum_q2:
            break

        elif sum_q1 > sum_q2:
            popped = q1.popleft()
            q2.append(popped)
            sum_q1 -= popped
            sum_q2 += popped
            answer += 1
            len_q1 -= 1

        elif sum_q1 < sum_q2:
            popped = q2.popleft()
            q1.append(popped)
            sum_q2 -= popped
            sum_q1 += popped
            answer += 1
            len_q2 -= 1

    if sum_q1 != sum_q2:
        answer = -1

    return answer


# 다른 사람 풀이 활용
# push, pop 과정을 실제로 거치지 않고 pointer 이동만으로 구현
def solution2(que1, que2):
    queSum = (sum(que1) + sum(que2))
    if queSum % 2:
        return -1
    target = queSum // 2

    n = len(que1)
    start = 0
    end = n - 1
    ans = 0

    cur = sum(que1)
    que3 = que1 + que2
    while cur != target:
        if cur < target:
            end += 1
            if end == n * 2:
                return -1
            cur += que3[end]
        else:
            cur -= que3[start]
            start += 1
        ans += 1
    return ans


# 입출력 예
input1_queue1 = [3, 2, 7, 2]
input1_queue2 = [4, 6, 5, 1]
print(solution(input1_queue1, input1_queue2))
# 2

input2_queue1 = [1, 2, 1, 2]
input2_queue2 = [1, 10, 1, 2]
print(solution(input2_queue1, input2_queue2))
# 7

input3_queue1 = [1, 1]
input3_queue2 = [1, 5]
print(solution(input3_queue1, input3_queue2))
# -1
