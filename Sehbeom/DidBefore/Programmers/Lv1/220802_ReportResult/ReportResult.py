# 2022.08.02
# 프로그래머스 lv1 / 신고 결과 받기

# 나의 풀이
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    reportNum = [0]*len(id_list)
    reportInfo = {}
    restrictedUser = []

    for oneReport in report:
        reportedId = oneReport.split(" ")

        if reportedId[0] in reportInfo:
            if (reportedId[1] in reportInfo[reportedId[0]]) == False:
                reportInfo[reportedId[0]].append(reportedId[1])
        else:
            reportedArray = [reportedId[1]]*1
            reportInfo[reportedId[0]] = reportedArray

    for oneReportInfo in reportInfo:
        for reportedPerUser in reportInfo[oneReportInfo]:
            if reportedPerUser in restrictedUser:
                continue
            else:
                reportNum[id_list.index(reportedPerUser)] += 1
                if reportNum[id_list.index(reportedPerUser)] >= k:
                    restrictedUser.append(reportedPerUser)

    for i in range(0, len(id_list)):
        if id_list[i] in reportInfo:
            for a in reportInfo[id_list[i]]:
                if a in restrictedUser:
                    answer[i] += 1

    return answer

# 다른 사람 풀이 활용


def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    numOfReport = {x: 0 for x in id_list}

    for oneReport in set(report):
        oneReportArray = oneReport.split(" ")
        numOfReport[oneReportArray[1]] += 1

    for oneReport in set(report):
        oneReportArray = oneReport.split(" ")
        if numOfReport[oneReportArray[1]] >= k:
            answer[id_list.index(oneReportArray[0])] += 1

    return answer


# 입출력 예
id_list_input1 = ["muzi", "frodo", "apeach", "neo"]
report_input1 = ["muzi frodo", "apeach frodo",
                 "frodo neo", "muzi neo", "apeach muzi"]
k_input1 = 2
# [2,1,1,0]

id_list_input2 = ["con", "ryan"]
report_input2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k_input2 = 3
# [0,0]

print(solution2(id_list_input1, report_input1, k_input1))
