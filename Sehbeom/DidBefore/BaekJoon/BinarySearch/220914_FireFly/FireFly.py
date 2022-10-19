# 2022.09.14
# 백준 / 3020 개똥벌레


def countTroubles(troubles, section, start, end):
    while start <= end:
        mid = (start+end)//2

        if start == end:
            mid = start if troubles[start] >= section else start+1
            break

        if troubles[mid] >= section:
            end = mid - 1

        elif troubles[mid] < section:
            start = mid + 1

    return mid


N, H = map(int, input().split())
sectionInfo = [0, H]
down = []
up = []
halfLen = N//2

for i in range(1, N+1):
    hurdle = int(input())
    if i % 2 == 1:
        down.append(hurdle)
        if not hurdle in sectionInfo:
            sectionInfo.append(hurdle)

    else:
        up.append(hurdle)
        if not (H-hurdle) in sectionInfo:
            sectionInfo.append(H-hurdle)

down.sort()
up.sort()
sectionInfo.sort()

downStart = 0
upStart = halfLen

minValue = halfLen
minSection = [sectionInfo[1], H-sectionInfo[-2]]

for i in range(2, len(sectionInfo)-1):
    if downStart < len(down):
        downStart = countTroubles(down, sectionInfo[i], downStart, halfLen - 1)

    upStart = countTroubles(up, H-sectionInfo[i]+1, 0, upStart - 1)

    sumTroubles = (halfLen-downStart) + (halfLen - upStart)

    if sumTroubles <= minValue:
        section = sectionInfo[i] - sectionInfo[i-1]
        if sumTroubles == minValue:
            minSection.append(section)
        else:
            minValue = sumTroubles
            minSection = [section]


numOfMin = 0
for m in minSection:
    numOfMin += m

print(minValue, numOfMin)
