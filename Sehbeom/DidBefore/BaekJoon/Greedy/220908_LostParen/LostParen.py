# 2022.09.08
# 백준 / 1541번 잃어버린 괄호

formular = input()

divideForm = []
oneChar = ""
for f in formular:
    if f == "+" or f == "-":
        divideForm.extend([int(oneChar), f])
        oneChar = ""
    else:
        oneChar += f
divideForm.append(int(oneChar))

answer = 0

isSub = False

for d in divideForm:
    if d == "+":
        isSub = True if isSub else False

    elif d == "-":
        isSub = True

    else:
        answer = (answer - d) if isSub else (answer + d)

print(answer)
