# 2022.09.22
# 백준 / 15903번 카드 합체 놀이

# 첫번째 풀었던 코드

n, m = map(int, input().split())
firstCards = list(map(int, input().split()))

for i in range(m):
    firstCards.sort()
    minSum = firstCards[0] + firstCards[1]
    firstCards[0] = minSum
    firstCards[1] = minSum

print(sum(firstCards))


# 두번째 풀었던 코드

# from collections import deque
# def checkProperIndex(value, cards):
#     start = 0
#     end = len(cards)-1
#     while start <= end:
#         mid = (start+end)//2

#         if cards[mid] == value:
#             return mid

#         elif cards[mid] > value:
#             end = mid-1

#         else:
#             start = mid+1

#     if cards[mid] < value:
#         mid += 1
#     return mid


# n, m = map(int, input().split())
# firstCards = list(map(int, input().split()))
# firstCards.sort()
# firstCards = deque(firstCards)

# for i in range(m):
#     minSum = firstCards.popleft() + firstCards.popleft()
#     if firstCards:
#         properIndex = checkProperIndex(minSum, firstCards)
#         firstCards.insert(properIndex, minSum)
#         firstCards.insert(properIndex, minSum)
#     else:
#         firstCards.extend([minSum, minSum])

# print(sum(firstCards))
