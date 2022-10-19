# 2022.09.08
# 프로그래머스 lv2 / 올바른 괄호

# 나의 풀이
def solution(s):
    if s[0] == ")":
        return False

    else:
        opened = 0
        isCorrect = True

        for i in s:
            if i == "(":
                opened += 1

            else:
                opened -= 1
                if opened == -1:
                    isCorrect = False

        if opened == 0 and isCorrect:
            return True
        else:
            return False


# 다른 사람 풀이 활용
def solution2(s):
    if s[0] == ")":
        return False

    else:
        opened = 0

        for i in s:
            if opened == -1:
                return False
            opened = opened + 1 if i == "(" else opened - 1

        return (opened == 0)


# 입출력 예
print(solution("()()"))
# True

print(solution("(())()"))
# True

print(solution(")()("))
# False

print(solution("(()("))
# False

print(solution("())(()"))
# False
