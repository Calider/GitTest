n = int(input())
mas = [[int(j) for j in input().split()] for i in range(n)]
for i in range(n//2):
    mas[i], mas[n-i-1] = mas[n-i-1], mas[i]

for i in range(n):
    for j in range(n):
        print(mas[i][j], end=' ')
    print()



