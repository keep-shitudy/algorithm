# 2022.10.19
# 프로그래머스 / Lv2 예상 대진표

def solution(n, a, b):
    answer = 1

    while ((a+1) // 2) != ((b+1) // 2):
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1

    return answer
