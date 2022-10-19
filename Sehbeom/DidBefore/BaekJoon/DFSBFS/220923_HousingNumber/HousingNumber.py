# 22.09.23
# 백준 / 2667번 단지번호 붙이기

connectCase = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def countHousingNumber(apt, pos):
    stack = [pos]
    apt[pos[1]][pos[0]] = 0
    numOfHouse = 1
    while stack:
        for c in connectCase:
            nextX = stack[-1][0] + c[0]
            nextY = stack[-1][1] + c[1]
            if nextX < 0 or nextX >= N or nextY < 0 or nextY >= N:
                continue

            if apt[nextY][nextX]:
                stack.append((nextX, nextY))
                apt[nextY][nextX] = 0
                numOfHouse += 1
                break
        else:
            stack.pop()

    return numOfHouse


N = int(input())
apartment = [[] for i in range(N)]

for i in range(N):
    apartment[i] = list(map(int, list(input())))

answer = []

for i in range(N):
    for j in range(N):
        if apartment[i][j]:
            answer.append(countHousingNumber(apartment, (j, i)))
answer.sort()
print(len(answer))
for a in answer:
    print(a)
