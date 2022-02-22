n = int(input())
mas = [[int(j) for j in input().split()] for i in range(n)]
priz = True
for i in range(n):
    if priz == False:
        break
    else:
        for j in range(n):
            if mas[i][j] == mas[j][i]:
                priz = True
            else:
                priz = False
                break
if priz == True:
    print('YES')
else:
    print('NO')
