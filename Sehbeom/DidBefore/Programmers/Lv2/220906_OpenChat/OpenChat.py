# 2022.09.06
# 프로그래머스 lv2 / 오픈 채팅방

# 나의 풀이
def solution(record):
    answer = []
    userProfile = {}

    for r in record:
        oneRecord = r.split()
        if oneRecord[0] == "Enter" or oneRecord[0] == "Change":
            userProfile[oneRecord[1]] = oneRecord[2]

    for r in record:
        oneRecord = r.split()
        if oneRecord[0] != "Change":
            info = "님이 들어왔습니다." if oneRecord[0] == "Enter" else "님이 나갔습니다."
            answer.append(userProfile[oneRecord[1]] + info)

    return answer

# 다른 사람 풀이 활용
# 모두 유사한 방식으로 해결


# 입출력 예
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
