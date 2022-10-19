# 2022.08.06
# 프로그래머스 lv1 / 소수 만들기


from itertools import combinations  # 다른 사람 풀이 활용

# 나의 풀이


def solution(nums):
    answer = 0
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                s = nums[i]+nums[j]+nums[k]
                for l in range(2, s):
                    if s % l == 0:
                        break
                    else:
                        if l == s-1:
                            answer += 1

    return answer


# 다른 사람 풀이 활용


def solution2(nums):
    answer = 0
    for c in combinations(nums, 3):
        comSum = sum(c)
        for s in range(2, int(comSum**0.5)+1):
            if comSum % s == 0:
                break

        else:
            answer += 1

    return answer


# 입출력 예
nums_input1 = [1, 2, 3, 4]

nums_input2 = [1, 2, 7, 6, 4]

print(solution2(nums_input2))
