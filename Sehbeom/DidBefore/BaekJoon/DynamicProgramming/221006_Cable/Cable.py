# 2022.10.06
# 백준 / 2565번 전깃줄

from audioop import cross


n = int(input())
cablePos = {}
crossInfo = {}
crossNumInfo = {}
totalCross = 0

for i in range(n):
    A, B = map(int, input().split())

    for c in cablePos:
        if ((A-c) * (B-cablePos[c])) < 0:
            totalCross += 1
            if A in crossInfo:
                crossInfo[A].append(c)
                crossNumInfo[A] += 1
            else:
                crossInfo[A] = [c]
                crossNumInfo[A] = 1

            if c in crossInfo:
                crossInfo[c].append(A)
                crossNumInfo[c] += 1
            else:
                crossInfo[c] = [A]
                crossNumInfo[c] = 1

            max(crossNumInfo, key=crossNumInfo.get)

    cablePos[A] = B

print(cablePos)
print(crossInfo)
print(crossNumInfo)
print(totalCross)
