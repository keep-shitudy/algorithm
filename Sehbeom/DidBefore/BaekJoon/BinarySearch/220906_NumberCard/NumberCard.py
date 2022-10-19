# 2022.09.06
# 백준 / 10815 숫자 카드

def isExist(cards, num, start, end):
    global a
    mid = (start+end)//2

    if (end - start) == 1:
        if num == cards[mid] or num == cards[mid+1]:
            a = 1
        return

    if num == cards[mid]:
        a = 1

    elif num > cards[mid]:
        isExist(cards, num, mid, end)

    elif num < cards[mid]:
        isExist(cards, num, start, mid)


N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))
answer = []
a = 0

cards.sort()

for n in numbers:
    isExist(cards, n, 0, len(cards)-1)
    answer.append(a)
    a = 0
print(*answer)

# 다른 사람 풀이
for n in numbers:
    a = 1 if n in cards else 0
    print(a, end=" ")
