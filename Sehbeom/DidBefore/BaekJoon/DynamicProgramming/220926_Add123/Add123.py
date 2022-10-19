# 2022.09.26
# 백준 / 9095번 1, 2, 3 더하기

def findAns(n):
    if n in result:
        return result[n]
    else:
        result[n] = findAns(n-1) + findAns(n-2) + findAns(n-3)
        return result[n]


result = {1: 1, 2: 2, 3: 4}

for i in range(int(input())):
    print(findAns(int(input())))
