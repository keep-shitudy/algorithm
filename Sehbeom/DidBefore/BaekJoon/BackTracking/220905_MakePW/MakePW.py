# 2022.09.05
# 백준 / 1759 암호 만들기

def makePW(stack, countV, countC, ptr):
    while ptr < C:
        oneAlph = alphabets[ptr]

        if (not stack) and (oneAlph == maxAlph):
            break

        stack.append(oneAlph)

        if oneAlph == 'a' or oneAlph == 'e' or oneAlph == 'i' or oneAlph == 'o' or oneAlph == 'u':
            countV += 1
        else:
            countC += 1

        if len(stack) == L:
            if countV >= 1 and countC >= 2:
                print(''.join(stack))

        else:
            makePW(stack, countV, countC, ptr+1)

        popped = stack.pop()

        if popped == 'a' or popped == 'e' or popped == 'i' or popped == 'o' or popped == 'u':
            countV -= 1
        else:
            countC -= 1
        ptr += 1


L, C = map(int, input().split())
alphabets = input().split()
alphabets.sort()
maxAlph = alphabets[C-L+1]

makePW([], 0, 0, 0)
