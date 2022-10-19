# 2022.08.18
# 백준 / 16953번 A->B

A, B = input().split(" ")
Blist = list(B)
answer = 1
canChange = False

while Blist:
    if "".join(Blist) == A:
        canChange = True
        Blist.clear()

    else:
        if Blist[len(Blist)-1] == "1":
            Blist.pop()
            answer += 1

        elif int(Blist[len(Blist)-1]) % 2 == 0:
            Btemp = int(int("".join(Blist)) / 2)
            Blist = list(str(Btemp))
            answer += 1

        else:
            Blist.clear()

if not canChange:
    answer = -1

print(answer)
