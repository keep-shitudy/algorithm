# 2022.09.22
# 백준 / 11497번 통나무 건너뛰기

# 정답 코드
# 최대값이 중앙에, 그 다음 두번째, 세번째로 큰 값을 이진 트리 형태로 오른쪽, 왼쪽에 두어야 함
# ex) 2 9 5 7 4
# -> 2 5 9 7 4
# -> 트리 형태로 보면
# ->     9
# ->   5   7
# ->  2     4
# 만약 두번째로 큰 값을 오른쪽, 세번째로 큰 값을 왼쪽에 두었다면 그 이후에도 더 큰 값이 오른쪽, 더 작은 값이 왼쪽으로 가야함.
# 그렇지 않으면 서로 인접한 통나무의 높이 차이가 더 커지게 됨.
# 이진 트리 형태로 구성한 후, 서로 인접한 통나무의 높이 차 중 최대값을 구하면 됨.
# 아래 코드에서는 이진 트리 형태가 아닌 내림차순 정렬 후, 인접한 통나무의 높이 차 구하는 과정을 인덱스로 구현함.
# <주석 1> 9 7 5 4 2 => 처음 9<->7, 9<->5 차이 중, 어차피 차이의 최대 값을 구해야 하므로 answer의 초기 값은 9<->5가 될 수 밖에 없음
# <주석 2> 이후 이진 트리 형태에서 인접한 요소끼리의 차를 구함 : 7<->4, 5<->2 등. 9<->7, 9<->5 는 앞에서 고려되었으므로 확인할 필요 없음
# <주석 3> 마지막으로 가장자리에 위치한 통나무들끼리의 차을 구한 후 비교 : logHeight[-2] - logHeight[-1]

T = int(input())

for t in range(T):
    N = int(input())
    logHeight = list(map(int, input().split()))
    logHeight.sort(reverse=True)
    answer = logHeight[0] - logHeight[2]  # <주석 1>

    for i in range(1, N-2):   # <주석 2>
        heightDiffer = logHeight[i] - logHeight[i+2]
        if answer < heightDiffer:
            answer = heightDiffer

    edgeDiffer = logHeight[-2] - logHeight[-1]  # <주석 3>
    if answer < edgeDiffer:
        answer = edgeDiffer

    print(answer)


# 처음 접근했던 방식
# 통나무 배열을 오름차순 정렬 후 중간 값과 최대값을 swap하면 될 것이라 생각함
# 하지만 정답은 최대값이 중앙에, 그 다음 두번째, 세번째로 큰 값을 이진 트리 형태로 오른쪽, 왼쪽에 두어야 함

    # if N % 2 == 1:
    #     temp = logHeight[(N-1)//2]
    #     logHeight[(N-1)//2] = logHeight[-1]
    #     logHeight[-1] = temp

    # else:
    #     leftCase = logHeight[(N-1)//2]
    #     rightCase = logHeight[(N-1)//2 + 1]
    #     leftCaseMax = logHeight[-1] - leftCase
    #     rightCaseMax = rightCase - logHeight[0]
    #     if leftCaseMax > rightCaseMax:
    #         logHeight[(N-1)//2 + 1] = logHeight[-1]
    #         logHeight[-1] = rightCase
    #     else:
    #         logHeight[(N-1)//2] = logHeight[-1]
    #         logHeight[-1] = leftCase

    # answer = logHeight[-1] - logHeight[0]
    # for i in range(len(logHeight)-1):
    #     heightDiffer = logHeight[i+1] - logHeight[i]
    #     if heightDiffer > answer:
    #         answer = heightDiffer

    # print(answer)
