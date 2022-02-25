vvod = input().split()
n = int(vvod[0])
m = int(vvod[1])
nn = 1
mas = [[0 for j in range(m)] for i in range(n)]
for j in range(m):
    mas[0][j] = nn
    nn += 1
i = 0
j = 0
mn = n
nm = m
while nn <= n * m:
    for i in range(n):
        if mas[i][m - 1] == 0:
            mas[i][m - 1] = nn
            nn += 1
    for j in range(m):
        if mas[n - 1][m-j-1] == 0:
            mas[n - 1][m-j-1] = nn
            nn += 1
    for i in range(n - 1):
        if mas[i - n + 1][mn - n] == 0:
            mas[i - n + 1][mn - n] = nn
            nn += 1
    for j in range(m - 1):
        if mas[nm - n - 1][j] == 0:
            mas[nm - n - 1][j] = nn
            nn += 1
    n -= 2
    m -= 2
def print_matrix(matrix):
    for i in range(mn):
        for j in range(nm):
            print(str(matrix[i][j]).ljust(3), end='')
        print()

print_matrix(mas)