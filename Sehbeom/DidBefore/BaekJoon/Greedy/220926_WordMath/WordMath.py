# 2022.09.26
# 백준 / 1339번 단어 수학


N = int(input())
charDic = {}

for i in range(N):
    temp = list(input())
    cipher = len(temp) - 1

    for j in range(cipher, -1, -1):
        oneChar = temp[cipher - j]
        if not oneChar in charDic:
            charDic[oneChar] = 10 ** j
        else:
            charDic[oneChar] += 10 ** j


charDic = dict(sorted(charDic.items(), key=lambda x: x[1], reverse=True))
charNum = 9
answer = 0

for c in charDic:
    answer += charDic[c] * charNum
    charNum -= 1

print(answer)
