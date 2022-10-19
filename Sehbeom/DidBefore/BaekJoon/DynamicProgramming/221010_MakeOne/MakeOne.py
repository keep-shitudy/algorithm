# 2022.10.10
# 백준 / 1463번 1로 만들기

N = int(input())
ansList = [0] * (N+1)
ansList[1] = 0

for i in range(2, N+1):
    if (i % 6) == 0:
        twoOrThree = min(ansList[int(i/2)], ansList[int(i/3)])
        ansList[i] = min(twoOrThree, ansList[i-1]) + 1
    elif (i % 3) == 0:
        ansList[i] = min(ansList[int(i/3)], ansList[i-1]) + 1
    elif (i % 2) == 0:
        ansList[i] = min(ansList[int(i/2)], ansList[i-1]) + 1
    else:
        ansList[i] = ansList[i-1]+1

print(ansList[N])
