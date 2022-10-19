# 2022.09.07
# 백준 / 12015 가장 긴 증가하는 부분 수열 2

# 내가 처음 풀었던 방식 -> 시간초과 O(N^2) 정도 나올 것으로 예상
# def findSeq(start, maxValueIndex):
#     global answer

#     curAns = 1
#     lastValue = A[start]
#     index = start+1
#     while (lastValue < maxValueInfo[maxValueIndex]) and (index < N):
#         a = A[index]
#         if a == maxValueInfo[maxValueIndex]:
#             lastValue = a
#             curAns += 1
#             maxValueIndex -= 1
#             if answer < curAns:
#                 answer = curAns

#             if (curAns-1) > (N-index-1):
#                 break

#             lastValue = A[start]
#             curAns = 1

#         elif a > lastValue:
#             lastValue = a
#             curAns += 1

#         index += 1


# N = int(input())
# A = list(map(int, input().split()))

# maxValueInfo = A[:]
# maxValueInfo.sort()

# answer = 0
# sliceIndex = 0

# while (answer < (N-sliceIndex-1)) and (sliceIndex < N):
#     findSeq(sliceIndex, N-1)
#     sliceIndex += 1

# print(answer)


# 구글링을 통해 알아본 방식
# 이분탐색 활용. Pypy3로 통과
# 자세한 설명 : https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-12015-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-2-%EA%B3%A8%EB%93%9C2-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89

N = int(input())
A = list(map(int, input().split()))

seqList = [A[0]]

for a in A:
    if seqList[-1] < a:
        seqList.append(a)

    else:
        start = 0
        end = len(seqList) - 1

        while start <= end:
            mid = (start + end)//2
            if seqList[mid] == a:
                start = mid
                break

            elif seqList[mid] < a:
                start = mid + 1

            elif seqList[mid] > a:
                end = mid - 1

        seqList[start] = a


print(len(seqList))
