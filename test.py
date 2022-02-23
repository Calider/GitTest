n = 8
mas = [['.']*n for j in range(n)]
kon = []
kon.extend(input())
kor = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
       '8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}
ik = kor[kon[1]]
jk = kor[kon[0]]
mas[ik][jk] = 'N'
for i in range(n):
        for j in range(n):
            if (jk - j) * (ik - i) == 2 or (jk - j) * (ik - i) == -2:
                try:
                    mas[i][j] = '*'
                except IndexError:
                    None

def print_matrix(matrix):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()

print_matrix(mas)