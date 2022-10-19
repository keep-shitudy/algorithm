# 2022.10.18
# 백준 / 1904번 01타일

# 처음 제출할 때 메모리 초과남. -> 배열 한칸 안에 너무 큰 수가 들어가서
# 중간 연산과정에 나머지 연산을 추가 -> 통과함.

N = int(input())

ansList = [0] * (N)
ansList[0] = 1


if N >= 2:
    ansList[1] = 2
    for i in range(2, N):
        ansList[i] = (ansList[i-1] + ansList[i-2]) % 15746

print(ansList[N-1])
