moved = False

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
        self.arr[y2][x2] = self.arr[y1][x1]
        self.arr[y1][x1] = '.' 
        global moved
        moved = True
        

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
        print('find_diag', y, x, find)
        i, j = y+1, x+1
        while i <= 7 and j <= 7:
            print('+++++',self.arr[i][j], i, j)
            if self.arr[i][j] == '.':
                pass
            elif self.arr[i][j] == find and (spec_x == None or spec_x == j) and (spec_y == None or spec_y == i):
                self.move(j, i, x, y)
            else:
                break
            i, j = i+1, j+1
        i, j = y+1, x-1
        while i <= 7 and j >= 0:
            print('+++++',self.arr[i][j], i, j)
            if self.arr[i][j] == '.':
                pass
            elif self.arr[i][j] == find and (spec_x == None or spec_x == j) and (spec_y == None or spec_y == i):
                self.move(j, i, x, y)
            else:
                break
            i, j = i+1, j-1
        i, j = y-1, x+1
        while i >= 0 and j <= 7:
            print('+++++',self.arr[i][j], i, j)
            if self.arr[i][j] == '.':
                pass
            elif self.arr[i][j] == find and (spec_x == None or spec_x == j) and (spec_y == None or spec_y == i):
                self.move(j, i, x, y)
            else:
                break
            i, j = i-1, j+1
        i, j = y-1, x-1
        while i >= 0 and j >= 0:
            print('-----',self.arr[i][j], i, j)
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
                if ord(spec_x)-97 == i[1]:
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
                if ord(spec_x)-97 == i[1]:
                    newmoves.append(i)
            moves = newmoves
            print(moves)
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
        
    def input_move(self, line, player):
        spec_x, spec_y = None, None
        kill = False
        if 'x' in line:
            line = line.replace('x', '')
            kill = True
            print(':::::', line, kill)
        if len(line) == 4:
            if GetType(line[1]) == 'str':
                spec_x = line[1]
            elif GetType(line[1]) == 'int':
                spec_y == line[1]
            newline = line[:1] + line[2:]
            line = newline
        print('speeeec', spec_x)
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

    def play(self):
        player = 1
        countmoves = 0
        while True:
            global moved
            moved = False
            line = input(f'Ход {player} игрока:')
            if line == 'exit':
                break
            self.input_move(line, player)
            if moved == True:
                countmoves += 1
                if player == 1:
                    player = 2
                else:
                    player = 1
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
            print('Победа 1 игрока')
            return True
        elif player2win:
            print('Победа 2 игрока')
            return True
        return False



f = field()

# f.input_move('e4', 1)
# f.input_move('g5', 2)
# f.input_move('d4', 1)
# f.input_move('f6', 2)
# f.input_move('Qh5', 1)
# f.input_move('Kf7', 2)

f.draw()
f.play()