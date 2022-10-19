# 2022.08.04
# 프로그래머스 lv1 / 신규 아이디 추천

# 나의 풀이

# ASCII Info
# a : 97, z : 122, 0 : 48, 9 : 57, - : 45, _ : 95, . : 46

import re


def solution(new_id):
    answer = 'a' if len(new_id) == 0 else new_id.lower()
    temp = []

    for i in range(0, len(answer)):
        asciiValue = ord(answer[i])
        if 45 <= asciiValue and asciiValue <= 122:
            if 45 <= asciiValue and asciiValue <= 57:
                if asciiValue == 47:
                    continue
                else:
                    if asciiValue == 46:
                        if len(temp) == 0 or temp[len(temp)-1] == '.':
                            continue
                    temp.append(answer[i])

            elif 95 <= asciiValue and asciiValue <= 122:
                if asciiValue == 96:
                    continue
                else:
                    temp.append(answer[i])
        else:
            continue

    if len(temp) >= 16:
        temp = temp[0:15]
    if len(temp) > 0 and temp[len(temp)-1] == '.':
        temp.pop(len(temp)-1)
    if len(temp) <= 2:
        if len(temp) == 0:
            temp.append('aaa')
        else:
            temp.extend([temp[len(temp)-1]*(3-len(temp))])

    answer = ''.join(temp)

    return answer


# 다른 사람 풀이 활용


def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + \
        "".join([st[-1] for i in range(3-len(st))])
    return st


# 입출력 예
new_id_input1 = "...!@BaT#*..y.abcdefghijklm"
# "bat.y.abcdefghi"

new_id_input2 = "z-+.^."
# "z--"

new_id_input3 = "=.="
# "aaa"

new_id_input4 = "123_.def"
# "123_.def"

new_id_input5 = "abcdefghijklmn.p"
# "abcdefghijklmn"

print(solution(new_id_input1))
