import random

fieldDraw = [['_' for i in range(10)] for j in range(10)]
fieldHide = [['0' for i in range(10)] for j in range(10)]

def Draw(fieldDraw):
    print('  1 2 3 4 5 6 7 8 9 10')
    for i in range(10):
        print(chr(65 + i), '' , end='')
        for j in range(10):
            print(fieldDraw[i][j], '', end='')
        print()

def CheckDir(x, y, size, field):
    countfree = 1
    dir = ['left', 'right', 'up', 'down']
    curdir = random.choice(dir)
    for i in range(4):
        if curdir == 'left' and x >= size-1:
            for j in range(1, size):
                if field[y][x-j] == '0':
                    countfree += 1
            if countfree == size:
                return curdir
        if curdir == 'right' and x <= 10-size:
            for j in range(1, size):
                if field[y][x+j] == '0':
                    countfree += 1
            if countfree == size:
                return curdir
        if curdir == 'up' and y >= size-1:
            for j in range(1, size):
                if field[y-j][x] == '0':
                    countfree += 1
            if countfree == size:
                return curdir
        if curdir == 'down' and y <= 10-size:
            for j in range(1, size):
                if field[y+j][x] == '0':
                    countfree += 1
            if countfree == size:
                return curdir
            
def ChangeField(x, y, dir, size, field):
    if dir == 'left':
        for i in range(size):
            field[y][x-i] = f'{size}'
    elif dir == 'right':
        for i in range(size):
            field[y][x+i] = f'{size}'
    elif dir == 'up':
        for i in range(size):
            field[y-i][x] = f'{size}'
    elif dir == 'down':
        for i in range(size):
            field[y+i][x] = f'{size}'

def SetShip(size):
    while True:
        x, y = random.randint(0, 9), random.randint(0, 9)
        if fieldHide[y][x] == '0':
            if size == 1:
                fieldHide[y][x] = '1'
                break
            else:
                curdir = CheckDir(x, y, size, fieldHide)
                if curdir != None:
                    ChangeField(x, y, curdir, size, fieldHide)
                    break

def Around(size):
    for i in range(10):
        for j in range(10):
            if fieldHide[i][j] == '0':
                change = False
                if -1 < i-1 < 10:
                    if fieldHide[i-1][j] == f'{size}':
                        change = True
                    if -1 < j + 1 < 10:
                        if fieldHide[i-1][j+1] == f'{size}':
                            change = True
                    if -1 < j - 1 < 10:
                        if fieldHide[i-1][j-1] == f'{size}':
                            change = True
                if -1 < i+1 < 10:
                    if fieldHide[i+1][j] == f'{size}':
                        change = True
                    if -1 < j-1 < 10:
                        if fieldHide[i+1][j-1] == f'{size}':
                            change = True
                    if -1 < j+1 < 10:
                        if fieldHide[i+1][j+1] == f'{size}':
                            change = True
                if -1 < j-1 < 10:
                        if fieldHide[i][j-1] == f'{size}':
                            change = True
                if -1 < j+1 < 10:
                        if fieldHide[i][j+1] == f'{size}':
                            change = True
                if change == True:
                    fieldHide[i][j] = '-'

def GenerateField():
    SetShip(4)
    Around(4)
    for i in range(2):
        SetShip(3)
        Around(3)
    for i in range(3):
        SetShip(2)
        Around(2)
    for i in range(4):
        SetShip(1)
        Around(1)

def CheckSunk(x, y, fieldHide, dir):
    sunk = True
    if -1 < x < 10 and -1 < y < 10:
        if fieldHide[y][x] == '1' or fieldHide[y][x] == '2' or fieldHide[y][x] == '3' or fieldHide[y][x] == '4':
            sunk = False
        if fieldHide[y][x] == 'P':
            if dir != 'x-1':
                if CheckSunk(x+1, y, fieldHide, 'x+1') == False:
                    sunk = False
            if dir != 'x+1':   
                if CheckSunk(x-1, y, fieldHide, 'x-1') == False:
                    sunk = False
            if dir != 'y-1':
                if CheckSunk(x, y+1, fieldHide, 'y+1') == False:
                    sunk = False
            if dir != 'y+1':
                if CheckSunk(x, y-1, fieldHide, 'y-1') == False:
                    sunk = False
    return sunk

def CheckWin(fieldHide):
    for i in range(10):
        for j in range(10):
            if fieldHide[i][j] == '1' or fieldHide[i][j] == '2' or fieldHide[i][j] == '3' or fieldHide[i][j] == '4':
                return False
    return True

def Play():
    while True:
        try:
            Draw(fieldDraw)
            inputline = input('Введите координаты выстрела(J5):')
            if inputline == 'exit':
                break
            if inputline == 'save':
                savefile = open('savefile.txt', 'w')
                for i in range(10):
                    for j in range(10):
                        savefile.write(f'{fieldDraw[i][j]}')
                        savefile.write(f'{fieldHide[i][j]}')
                savefile.close()
                break
            letter, numb = inputline[0], int(inputline[1])
            if inputline[1:3] == '10':
                numb = 10
            if letter < 'A' or letter > 'J' or numb < 1 or numb > 10:
                numb = int(';)')
            x, y = numb - 1, ord(letter) - 65
            if fieldHide[y][x] == '0' or fieldHide[y][x] == '-':
                print('Промах!')
                fieldDraw[y][x] = 'X'
            else:
                print('Попадание!')
                fieldDraw[y][x] = 'O'
                fieldHide[y][x] = 'P'
                if CheckSunk(x, y, fieldHide, '0') == True:
                    print('Корабль потоплен!')
                    if CheckWin(fieldHide) == True:
                        Draw(fieldDraw)
                        print('Победа!')
                        break
        except:
            print('Ошибка ввода!')

def StartNewGame():
    GenerateField()
    print('Для выхода в любой момент введите exit')
    print('Для сохранения во время игры введите:save')
    Play()


if input('Чтобы загрузить сохранение, введите load, иначе нажмите Enter:') == 'load':
    try:
        file = open('savefile.txt', 'r')
        line = file.readline()
        count = 0
        for i in range(10):
            for j in range(10):
                fieldDraw[i][j] = line[count]
                count += 1
                fieldHide[i][j] = line[count]
                count += 1
        print('Для выхода в любой момент введите exit')
        print('Для сохранения во время игры введите:save')
        Play()
    except:
        print('Произошла ошибка, запуск новой игры...')
        StartNewGame()
else:
    StartNewGame()

#pswork