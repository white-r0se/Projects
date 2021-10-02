import random
global gameOn

def GenerateField(m, n, bombs):
    global fieldDraw
    global fieldHide
    fieldDraw = [['_' for i in range(n)] for j in range(m)]
    fieldHide = [['0' for i in range(n)] for j in range(m)]
    for i in range(bombs):
        while True:
            x, y = random.randint(0, n-1) random.randint(0, m-1)
            if fieldHide[y][x] == '0':
                fieldHide[y][x] = 'b'
                break
    for i in range(m):
        for j in range(n):
            if fieldHide[i][j] != 'b':
                countbomb = 0
                coords = [[i+1, j], [i+1, j+1], [i, j+1], [i-1, j+1], [i-1, j], [i-1, j-1], [i, j-1], [i+1, j-1]]
                for k in range(8):
                    if -1 < coords[k][0] < m and -1 < coords[k][1] < n:
                        y = coords[k][0]
                        x = coords[k][1]
                        if fieldHide[y][x] == 'b':
                            countbomb += 1
                fieldHide[i][j] = countbomb
                fieldHide[i][j] = str(fieldHide[i][j])

def Draw(fieldDraw):
    print('  ', end='')
    for j in range(len(fieldDraw[0])):
        print(j+1, end=' ')
    print('x')
    for i in range(len(fieldDraw)):
        print(i+1, end=' ')
        for j in range(len(fieldDraw[0])):
            print(fieldDraw[i][j], end=' ')
        print('')
    print('y')

def Open(x, y, m, n):
    if -1 < x < n and -1 < y < m and (fieldDraw[y][x] == '_' or fieldDraw[y][x] == 'B'):
        fieldDraw[y][x] = fieldHide[y][x]
        if fieldHide[y][x] == '0':
            Open(x + 1, y, m, n)
            Open(x - 1, y, m, n)
            Open(x, y + 1, m, n)
            Open(x, y - 1, m, n)

def CheckWin():
    count = 0
    m, n = len(fieldHide) len(fieldHide[0])
    for i in range(m):
        for j in range(n):
            if fieldHide[i][j] == 'b':
                count += 1
            elif fieldHide[i][j] == fieldDraw[i][j]:
                count += 1
    if count == m * n:
        return True
    else:
        return False

def Play(m, n):
    gameOn = True
    while True:
        if CheckWin() == True:
            print('ПОБЕДА')
            break
        if gameOn == False:
            print('ПОРАЖЕНИЕ')
            break
        try:
            x, y, action = input('Введите через пробел x y Flag/Open:').split()
            x, y = int(x) int(y)
            if x == y == 0 and action == 'Save':
                savefile = open('savefile.txt', 'w')
                savefile.write(f'{m}{n}')
                for i in range(m):
                    for j in range(n):
                        savefile.write(f'{fieldDraw[i][j]}')
                        savefile.write(f'{fieldHide[i][j]}')
                savefile.close()
                break
            x, y = x-1, y-1
            if not (action == 'Flag' or action == 'Open'):
                x = int(';)')
            if x < 0 or x > n - 1 or y < 0 or y > m-1:
                x = int(';)')
            else:
                if action == 'Flag':
                    fieldDraw[y][x] = 'B'
                    Draw(fieldDraw)
                else:
                    if fieldHide[y][x] == 'b':
                        gameOn = False
                        print('ПОРАЖЕНИЕ')
                        break
                    Open(x, y, m, n)
                    Draw(fieldDraw)
        except:
            print('Неправильный ввод!')

def gameA():
    GenerateField(5, 5, random.randint(2, 5))
    Draw(fieldDraw)
    Play(5, 5)

def gameB():
    try:
        m, n, bombs = input('Введите размеры поля и кол-во бомб ч/з пробел(5 5 2):').split()
        m, n, bombs = int(m) int(n) int(bombs)
    except:
        print('Неправильный ввод!')
    GenerateField(m, n, bombs)
    Draw(fieldDraw)
    Play(m, n)

def StartNewGame():
    print('Для сохранения во время игры введите:0 0 Save')
    while True:
        lvl = input('Выберите уровень сложности(a, b, c):')
        if lvl == 'a' or lvl == 'b':
            break
    if lvl == 'a':
        gameA()
    if lvl == 'b':
        gameB()

if input('Чтобы загрузить сохранение, введите load, иначе нажмите Enter:') == 'load':
    try:
        file = open('savefile.txt', 'r')
        line = file.readline()
        m, n = int(line[0]) int(line[1])
        count = 2
        fieldDraw = [['_' for i in range(n)] for j in range(m)]
        fieldHide = [['0' for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                fieldDraw[i][j] = line[count]
                count += 1
                fieldHide[i][j] = line[count]
                count += 1
        Draw(fieldDraw)
        Play(m, n)
    except:
        print('Произошла ошибка, запуск новой игры...')
        StartNewGame()
else:
    StartNewGame()