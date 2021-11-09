
class field:
    def __init__(self) -> None:
        self.arr = [[' ' for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if i % 2 == 0 and j % 2 == 1:
                    self.arr[i][j] = 'O'
                elif i % 2 == 1 and j % 2 == 0:
                    self.arr[i][j] = 'X'
    
    def Draw(self):
        print('  1 2 3 4 5 6 7 8 9')
        for i in range(9):
            print(chr(65 + i), '' , end='')
            for j in range(9):
                print(self.arr[i][j], end=' ')
            print()

    def SetBridge(self, y, x, player):
        if self.arr[y][x] == '-' or self.arr[y][x] == '|':
            raise ValueError
        elif self.arr[y][x] != ' ':
            raise NameError
        if player == 1:
            if self.arr[y][NewCoordForSet(x, '+')] == 'X' or self.arr[y][NewCoordForSet(x, '-')] == 'X':
                self.arr[y][x] = '-'
            else:
                self.arr[y][x] = '|'
        else:
            if self.arr[y][NewCoordForSet(x, '-')] == 'O' or self.arr[y][NewCoordForSet(x, '+')] == 'O':
                self.arr[y][x] = '-'
            else:
                self.arr[y][x] = '|'

    def CheckWin(self, player):
        for i in range(1, 9, 2):
            if player == 1:
                if CheckWinOne(self.arr, i, 0):
                    return True
            else:
                if CheckWinOne(self.arr, 0, i):
                    return True

def CheckWinOne(arr, y, x, last=0):
    if y > 8 or y < 0 or x > 8 or x < 0:
        return False
    if y == 8 or x == 8:
        return True
    if arr[NewCoordForSet(y, '-')][x] == '|' and last != 'down':
        if CheckWinOne(arr, y-2, x, 'up'):
            return True
    if arr[NewCoordForSet(y, '+')][x] == '|' and last != 'up':
        if CheckWinOne(arr, y+2, x, 'down'):
            return True
    if arr[y][NewCoordForSet(x, '-')] == '-' and last != 'right':
        if CheckWinOne(arr, y, x-2, 'left'):
            return True
    if arr[y][NewCoordForSet(x, '+')] == '-' and last != 'left':
        if CheckWinOne(arr, y, x+2, 'right'):
            return True

def Play(f, player=1):
    while True:
        try:
            f.Draw()
            print(player)
            print(f'Ход {player} игрока')
            inputline = input('Введите координату хода (например, B2):')
            if inputline == 'exit':
                break
            if inputline == 'save':
                savefile = open('savefile_most.txt', 'w')
                for i in range(9):
                    for j in range(9):
                        savefile.write(f'{f.arr[i][j]}')
                savefile.write(f'{player}')
                savefile.close()
                break
            letter, numb = inputline[0], int(inputline[1])
            if letter < 'A' or letter > 'I' or numb < 1 or numb > 9:
                raise KeyError
            x, y = numb - 1, ord(letter) - 65
            f.SetBridge(y, x, player)
            if f.CheckWin(player):
                f.Draw()
                print(f'Победа {player} игрока!')
                break
        except ValueError:
            print('На этом месте уже стоит мост!')
        except KeyError:
            print('Ошибка с вводом координаты!')
        except NameError:
            print('Нельзя ставить мост на камень!')
        else:
            if player == 1:
                player = 2
            else:
                player = 1

def NewCoordForSet(value, sign):
    if sign == '+':
        if -1 < value + 1 < 9:
            return value + 1
    elif sign == '-':
        if -1 < value - 1 < 9:
            return value - 1
    return value

def StartNewGame():
    f = field()
    print('Для выхода в любой момент введите exit')
    print('Для сохранения во время игры введите save')
    Play(f)


if input('Чтобы загрузить сохранение, введите load, иначе нажмите Enter:') == 'load':
    try:
        file = open('savefile_most.txt', 'r')
        line = file.readline()
        count = 0
        f = field()
        for i in range(9):
            for j in range(9):
                f.arr[i][j] = line[count]
                count += 1
        player = int(line[count])
    except FileNotFoundError:
        print('Произошла ошибка, сохрание отсутствует, запуск новой игры...')
        StartNewGame()
    else:
        print('Для выхода в любой момент введите exit')
        print('Для сохранения во время игры введите:save')
        Play(f, player)
else:
    StartNewGame()

