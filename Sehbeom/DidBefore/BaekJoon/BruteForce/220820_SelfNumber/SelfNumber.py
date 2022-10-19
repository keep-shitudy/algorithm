# 2022.08.20
# 백준 / 4673번 Self Number

def findSelfNum(allNumInfo, curNum):
    if curNum <= 10000:
        numEachSum = sum(map(int, list(str(curNum))))
        dN = curNum + numEachSum
        allNumInfo[dN] = False
        findSelfNum(allNumInfo, dN)


allNumInfo = {x: True for x in range(1, 10001)}

curNum = 1

while curNum <= 10000:
    if not allNumInfo[curNum]:
        curNum += 1
        continue

    findSelfNum(allNumInfo, curNum)
    curNum += 1

for i in range(1, 10001):
    if allNumInfo[i]:
        print(i)
