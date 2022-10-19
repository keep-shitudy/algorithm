# 2022.08.05
# 프로그래머스 lv1 / 숫자 문자열과 영단어

# 나의 풀이
def solution(s):
    numberInfo = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    # a~z : 97~122, 0~9:48~57
    temp = []
    answer = []
    for i in range(0, len(s)):
        asciiNum = ord(s[i])
        if 97 <= asciiNum and asciiNum <= 122:
            temp.append(s[i])
            if ''.join(temp) in numberInfo:
                answer.append(numberInfo[''.join(temp)])
                temp.clear()
        elif 48 <= asciiNum <= 57:
            answer.append(s[i])
    return int(''.join(answer))

# 다른 사람 풀이 활용


def solution2(s):
    numberInfo = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    for key, value in numberInfo.items():
        s = s.replace(key, value)

    return s


# 입출력 예
s_input1 = "one4seveneight"
# 1478

s_input2 = "23four5six7"
# 234567

s_input3 = "2three45sixseven"
# 234567

s_input4 = "123"
# 123

print(solution(s_input3))
