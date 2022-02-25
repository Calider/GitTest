vvod = input().split()
n = int(vvod[0])
m = int(vvod[1])
nn = 1
mas = [[0 for j in range(m)] for i in range(n)]
scol = 0
endcol = m - 1
srow = 0
endrow = n - 1
if n != 1 and m != 1:
    while nn != n * m + 1:
        for i in range(scol, endcol + 1):
            mas[srow][i] = nn
            nn += 1
        srow +=1
        for j in range(srow, endrow + 1):
            mas[j][endcol] = nn
            nn += 1
        endcol -= 1
        for i in range(endcol, scol - 1, -1):
            mas[endrow][i] = nn
            nn += 1
        endrow -=1
        for j in range(endrow, srow - 1, -1):
            mas[j][scol] = nn
            nn += 1
        scol += 1
elif n == 1:
    for i in range(m):
        mas[0][i] = nn
        nn += 1
else:
    for i in range(m):
        for j in range(n):
            mas[j][0] = nn
            nn += 1

def print_matrix(matrix):
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end='')
        print()

print_matrix(mas)