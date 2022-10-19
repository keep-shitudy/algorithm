# 2022.10.04
# 백준 / 11052번 카드 구매하기

# 내가 푼 코드
# N = int(input())
# cards = list(map(int, input().split()))

# answer = 0
# DN = [0] * N
# DN[0] = cards[0]

# for i in range(1, len(cards)):
#     start = -1
#     end = i
#     newOne = 0
#     while start < end:
#         start += 1
#         end -= 1
#         if start == end:
#             if newOne < (DN[start] * 2):
#                 newOne = DN[start] * 2
#         else:
#             if newOne < (DN[start] + DN[end]):
#                 newOne = DN[start] + DN[end]

#     if newOne < cards[i]:
#         DN[i] = cards[i]
#         answer = cards[i]
#     else:
#         DN[i] = newOne
#         answer = newOne


# print(answer)

# 다른 사람의 코드
# 방식은 동일하나 더 쉽게 풀 수 있음
N = int(input())
cards = [0]
cards += list(map(int, input().split()))

DN = [0] * (N+1)
DN[1] = cards[1]
DN[2] = max(cards[2], cards[1]*2)

for i in range(3, N+1):
    DN[i] = cards[i]
    for j in range(1, i//2 + 1):
        DN[i] = max(DN[i], DN[j] + DN[i-j])

print(DN[N])
