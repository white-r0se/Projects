moved = False
import copy

def get_coord(coord):
    return (ord(coord[0])-97, int(coord[1])-1)  

def GetType(x):
    try:
        newx = int(x)
        if str(newx) == x:
            return 'int'
        elif newx == x:
            return 'int'
    except ValueError:
        pass
    return 'str'
    

class field: 
    def __init__(self) -> None:
        self.arr = [[' ' for j in range(8)] for i in range(8)]
        for i in range(2, 6):
            for j in range(8):
                self.arr[i][j] = '.'
        self.arr[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        self.arr[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        for i in range(8):
            self.arr[1][i] = 'P'
            self.arr[6][i] = 'p'
        self.player1_not = {'K':False, 'R':[False, False]}
        self.player2_not = {'K':False, 'R':[False, False]}
        self.record = []

    def draw(self):
        print('   A B C D E F G H')
        print()
        for i in range(7, -1, -1):
            print(i+1, end='  ')
            for j in range(8):
                print(self.arr[i][j], end=' ')
            print('  ', i+1)
        print()
        print('   A B C D E F G H')

    def move(self, x1, y1, x2, y2):
        print('[', y1, x1, '] [', y2, x2, ']')
        print(self.arr[y1][x1], '->', self.arr[y2][x2])
        if self.arr[y2][x2] != '.':
            if self.arr[y1][x1] == self.arr[y1][x1].lower() and self.arr[y2][x2] == self.arr[y2][x2].lower():
                return None
            elif self.arr[y1][x1] == self.arr[y1][x1].upper() and self.arr[y2][x2] == self.arr[y2][x2].upper():
                return None
        self.arr[y2][x2] = self.arr[y1][x1]
        self.arr[y1][x1] = '.' 
        global moved
        moved = True
        if (x1 == 4 and y1 == 0):
            self.player1_not['K'] = True
        elif (x1 == 4 and y1 == 7):
            self.player2_not['K'] = True
        elif (x1 == 0 and y1 == 0):
            self.player1_not['R'][0] = True
        elif (x1 == 7 and y1 == 0):
            self.player1_not['R'][1] == True
        elif (x1 == 0 and y1 == 7):
            self.player2_not['R'][0] == True
        elif (x1 == 7 and y1 == 7):
            self.player2_not['R'][1] == True        

    def find_straight(self, find, x, y, spec_x, spec_y):
        for i in range(x+1, 8):
            if self.arr[y][i] == '.':
                pass
            elif self.arr[y][i] == find and (spec_x == None or spec_x == i) and (spec_y == None or spec_y == y):
                self.move(i, y, x, y)
            else:
                break
        for i in range(x-1, -1, -1):
            if self.arr[y][i] == '.':
                pass
            elif self.arr[y][i] == find and (spec_x == None or spec_x == i) and (spec_y == None or spec_y == y):
                self.move(i, y, x, y)
            else:
                break
        for i in range(y+1, 8):
            if self.arr[i][x] == '.':
                pass
            elif self.arr[i][x] == find and (spec_x == None or spec_x == x) and (spec_y == None or spec_y == i):
                self.move(x, i, x, y)
            else:
                break
        for i in range(y-1, -1, -1):
            if self.arr[i][x] == '.' and (spec_x == None or spec_x == x) and (spec_y == None or spec_y == i):
                pass
            elif self.arr[i][x] == find:
                self.move(x, i, x, y)
            else:
                break

    def find_diagonal(self, find, x, y, spec_x, spec_y):
        i, j = y+1, x+1
        while i <= 7 and j <= 7:
            if self.arr[i][j] == '.':
                pass
            elif self.arr[i][j] == find and (spec_x == None or spec_x == j) and (spec_y == None or spec_y == i):
                self.move(j, i, x, y)
            else:
                break
            i, j = i+1, j+1
        i, j = y+1, x-1
        while i <= 7 and j >= 0:
            if self.arr[i][j] == '.':
                pass
            elif self.arr[i][j] == find and (spec_x == None or spec_x == j) and (spec_y == None or spec_y == i):
                self.move(j, i, x, y)
            else:
                break
            i, j = i+1, j-1
        i, j = y-1, x+1
        while i >= 0 and j <= 7:
            if self.arr[i][j] == '.':
                pass
            elif self.arr[i][j] == find and (spec_x == None or spec_x == j) and (spec_y == None or spec_y == i):
                self.move(j, i, x, y)
            else:
                break
            i, j = i-1, j+1
        i, j = y-1, x-1
        while i >= 0 and j >= 0:
            if self.arr[i][j] == '.':
                pass
            elif self.arr[i][j] == find and (spec_x == None or spec_x == j) and (spec_y == None or spec_y == i):
                self.move(j, i, x, y)
            else:
                break
            i, j = i-1, j-1

    def king(self, find, x, y, spec_x, spec_y):
        moves = [[y, x-1], [y, x+1], [y+1, x], [y-1, x], [y-1, x+1], [y-1, x-1], [y+1, x-1], [y+1, x+1]]
        if spec_x != None:
            newmoves = []
            for i in moves:
                if spec_x == i[1]:
                    newmoves.append(i)
            moves = newmoves
        elif spec_y != None:
            newmoves = []
            for i in moves:
                if spec_y == i[0]:
                    newmoves.append(i)
            moves = newmoves
        newmoves = []
        for i in moves:
            ytest, xtest = i
            if 0 <= ytest <= 7 and 0 <= xtest <= 7:
                newmoves.append(i)
        moves = newmoves
        for move in moves:
            try:
                if self.arr[move[0]][move[1]] == find:
                    self.move(move[1], move[0], x, y)
                    break
            except IndexError: pass
    
    def queen(self, find, x, y, spec_x, spec_y):
        self.find_straight(find, x, y, spec_x, spec_y)
        self.find_diagonal(find, x, y, spec_x, spec_y)

    def rook(self, find, x, y, spec_x, spec_y):
        self.find_straight(find, x, y, spec_x, spec_y)

    def bishop(self, find, x, y, spec_x, spec_y):
        self.find_diagonal(find, x, y, spec_x, spec_y)

    def knight(self, find, x, y, spec_x, spec_y):
        moves = [[y+2, x-1], [y+2, x+1], [y+1, x+2], [y-1, x+2], [y-2, x+1], [y-2, x-1], \
        [y-1, x-2], [y+1, x-2]]
        if spec_x != None:
            newmoves = []
            for i in moves:
                if spec_x == i[1]:
                    newmoves.append(i)
            moves = newmoves
        elif spec_y != None:
            newmoves = []
            for i in moves:
                if spec_y == i[0]:
                    newmoves.append(i)
            moves = newmoves
        for move in moves:
            try:
                if self.arr[move[0]][move[1]] == find:
                    self.move(move[1], move[0], x, y)
            except IndexError: pass
        
    def input_move(self, line, player, spec_x=None, spec_y=None):
        kill = False
        if '+' in line:
            line = line.replace('+', '')
        if 'x' in line:
            line = line.replace('x', '')
            kill = True
        if '!' in line:
            line = line.replace('!', '')
        if line == 'O-O':
            if player == 1 and self.player1_not['K'] == False and self.player1_not['R'][1] == False and \
                self.arr[0][5] == '.' and self.arr[0][6] == '.':
                self.move(4, 0, 6, 0)
                self.move(7, 0, 5, 0)
            elif player == 2 and self.player2_not['K'] == False and self.player2_not['R'][1] == False and \
                self.arr[7][5] == '.' and self.arr[7][6] == '.':
                self.move(4, 7, 6, 7)
                self.move(7, 7, 5, 7)
        if line == 'O-O-O':
            if player == 1 and self.player1_not['K'] == False and self.player1_not['R'][0] == False and \
                self.arr[0][2] == '.' and self.arr[0][3] == '.':
                self.move(4, 0, 2, 0)
                self.move(0, 0, 3, 0)
            elif player == 2 and self.player2_not['K'] == False and self.player2_not['R'][0] == False and \
                self.arr[7][2] == '.' and self.arr[7][3] == '.':
                self.move(4, 7, 2, 7)
                self.move(0, 7, 3, 7)
        if len(line) == 3 and line[0].lower() == line[0]:
            if GetType(line[0]) == 'str':
                spec_x = ord(line[0])-97
            elif GetType(line[0]) == 'int':
                spec_y == line[0]
            newline = line[1:]
            line = newline
        elif len(line) == 4:
            if GetType(line[1]) == 'str':
                spec_x = ord(line[1])-97
            elif GetType(line[1]) == 'int':
                spec_y == line[1]
            newline = line[:1] + line[2:]
            line = newline
        if len(line) == 2:
            x, y = get_coord(line)
            if kill == False and self.arr[y][x] != '.':
                return False
            if player == 1:
                if kill == False:
                    if 0 <= y-2 <= 7:
                        if y == 3 and self.arr[y-2][x] == 'P' and (spec_x == None or spec_x == x) and (spec_y == None or spec_y == y-2):
                            self.move(x, y-2, x, y)
                        elif self.arr[y-1][x] == 'P' and (spec_x == None or spec_x == x) and (spec_y == None or spec_y == y-1):
                            self.move(x, y-1, x, y)
                    elif 0 <= y-1 <= 7:
                        if self.arr[y-1][x] == 'P' and (spec_x == None or spec_x == x) and (spec_y == None or spec_y == y-1):
                            self.move(x, y-1, x, y)
                elif kill == True:
                    if 0 <= y-1 <= 7 and 0 <= x-1 <= 7:
                        if self.arr[y-1][x-1] == 'P' and (spec_x == None or spec_x == x-1) and (spec_y == None or spec_y == y-1):
                            self.move(x-1, y-1, x, y)
                        elif 0 <= y-1 <= 7 and 0 <= x+1 <= 7:
                            if self.arr[y-1][x+1] == 'P' and (spec_x == None or spec_x == x+1) and (spec_y == None or spec_y == y-1):
                                self.move(x+1, y-1, x, y)
                    elif 0 <= y-1 <= 7 and 0 <= x+1 <= 7:
                            if self.arr[y-1][x+1] == 'P' and (spec_x == None or spec_x == x+1) and (spec_y == None or spec_y == y-1):
                                self.move(x+1, y-1, x, y)
            elif player == 2:
                if kill == False:
                    if y == 4 and self.arr[y+2][x] == 'p' and kill == False:
                        self.move(x, y+2, x, y)
                    elif self.arr[y+1][x] == 'p' and kill == False:
                        self.move(x, y+1, x, y)
                elif kill == True:
                    if self.arr[y+1][x-1] == 'p' and (spec_x == None or spec_x == x-1) and (spec_y == None or spec_y == y-1):
                        self.move(x-1, y+1, x, y)
                    elif self.arr[y+1][x+1] == 'p' and (spec_x == None or spec_x == x+1) and (spec_y == None or spec_y == y-1):
                        self.move(x+1, y+1, x, y)
        elif len(line) == 3:
            if line[0] == 'K':
                x, y = get_coord(line[1:])
                if player == 1:
                    find = 'K'
                elif player == 2:
                    find = 'k'
                self.king(find, x, y, spec_x, spec_y)
            elif line[0] == 'Q':
                x, y = get_coord(line[1:])
                if player == 1:
                    find = 'Q'
                elif player == 2:
                    find = 'q'
                self.queen(find, x, y, spec_x, spec_y)
            elif line[0] == 'R':
                x, y = get_coord(line[1:])
                if player == 1:
                    find = 'R'
                elif player == 2:
                    find = 'r'
                self.rook(find, x, y, spec_x, spec_y)
            elif line[0] == 'B':
                x, y = get_coord(line[1:])
                if player == 1:
                    find = 'B'
                elif player == 2:
                    find = 'b'
                self.bishop(find, x, y, spec_x, spec_y)
            elif line[0] == 'N':
                x, y = get_coord(line[1:])
                if player == 1:
                    find = 'N'
                elif player == 2:
                    find = 'n'
                self.knight(find, x, y, spec_x, spec_y)

    def play(self, player=1, countmoves=0):
        print('Для сохранение введите save, для выхода exit')
        while True:
            global moved
            moved = False
            line = input(f'Ход {player} игрока:')
            if line == 'exit':
                break
            if line == 'save':
                with open('chess_local_save.txt', 'w') as newfile:
                    for i in range(len(self.record)):
                        print(f'{i+1}. {self.record[i][0]} {self.record[i][1]}', file=newfile)
                break
            self.input_move(line, player)
            if moved == True:
                countmoves += 1
                if player == 1:
                    player = 2
                    self.record.append([line, None])
                else:
                    player = 1
                    if self.record != []:
                        self.record[-1][1] = line
            self.draw()
            if self.check_win():
                print('Число ходов:', int(countmoves/2+0.5))
                break

    
    def check_win(self):
        player1win, player2win = True, True
        for line in self.arr:
            for i in line:
                if i == 'k':
                    player1win = False
                elif i == 'K':
                    player2win = False
        if player1win:
            self.draw()
            print('Победа 1 игрока')
            return True
        elif player2win:
            self.draw()
            print('Победа 2 игрока')
            return True
        return False

    def readfile(self, file, fullform=False):
        lines = file.readlines()
        curmove = 0
        c = 0
        player = 1
        cache = []
        cache.append(copy.deepcopy(self.arr))
        self.draw()
        print(f'Ход №{curmove}')
        while True:
            print('n - движение вперед, p - движение назад, play - начать игру с этого момента, exit - выход')
            inp = input()
            if inp == 'exit':
                break
            elif inp == 'n':
                nmove, move1, move2 = lines[curmove].split()
                print(move1, move2)
                if fullform == False:
                    if player == 1:
                        self.input_move(move1, player)
                        player = 2
                        self.record.append([move1, None])
                    else:
                        self.input_move(move2, player)
                        player = 1
                        self.record[-1][1] = move2
                elif fullform == True:
                    if player == 1:
                        self.fullformat_input(move1, player)
                        player = 2
                    elif player == 2:
                        self.fullformat_input(move2, player)
                        player = 1
                c += 1
                self.draw()
                print('C', c)
                print(f'Ход №{curmove+1}')
                if c % 2 == 0:
                    curmove += 1
                cache.append(copy.deepcopy(self.arr))
            elif inp == 'p':
                if c % 2 == 0:
                    curmove -= 1
                c -= 1
                self.arr = copy.deepcopy(cache[c])
                f.draw()
                print(f'Ход №{curmove+1}')
                if player == 1:
                    player = 2
                    if fullform == False:
                        self.record[-1][1] = None
                else:
                    player = 1
                    if fullform == False:
                        del self.record[-1]
            elif inp == 'play':
                self.play(player, c)
                break

    def fullformat_input(self, move, player):
        if '-' in move:
            left, right = move.split('-')
            if len(left) == 3:
                spec_x, spec_y = get_coord(left[1:])
                self.input_move(f'{left[0]}{right}', player, spec_x, spec_y)
            elif len(left) == 2:
                spec_x, spec_y = get_coord(left)
                self.input_move(right, player, spec_x, spec_y)
        elif 'x' in move:
            left, right = move.split('x')
            if len(left) == 3:
                spec_x, spec_y = get_coord(left[1:])
                self.input_move(f'{left[0]}x{right}', player, spec_x, spec_y)
            elif len(left) == 2:
                spec_x, spec_y = get_coord(left)
                self.input_move(right, player, spec_x, spec_y)

f = field()

# with open('chess_local_save.txt', 'r') as File:
#     f.readfile(File)

with open('chess_save_fullformat.txt', 'r') as File:
    f.readfile(File, fullform=True)

# with open('chess_save2.txt', 'r') as File:
#     f.readfile(File)