field = [['13', '14', '__', '15'], [' 9', '10' , '11', '12'], [' 5', ' 6' , ' 7', ' 8'], [' 1', ' 2', ' 3', ' 4']]
fieldWin = [['13', '14', '15', '__'], [' 9', '10' , '11', '12'], [' 5', ' 6' , ' 7', ' 8'], [' 1', ' 2', ' 3', ' 4']]
count_moves = 0

def Draw():
    print(field[3], field[2], field[1], field[0], sep = '\n')
    
def FindCoordinate(elem, field):
    for i in range(4):
        try:
            x = field[i].index(elem)
            if -1 < x < 4:
                return (i, x)
        except:
            pass       

def ValuableElement(field):
    result = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    x, y = FindCoordinate('__', field)
    if x + 1 <= 3:
        result[0] = [x + 1, y]
    if y + 1 <= 3:
        result[1] = [x, y + 1]
    if x - 1 >= 0:
        result[2] = [x - 1, y]
    if y - 1 >= 0:
        result[3] = [x, y - 1]
    return result

Draw()

while True:
    while True:
        try:
            kost = input('Введите костяшку, которую хотите передвинуть:')
            if len(kost) == 1:
                kost = f' {kost}'
            x, y = FindCoordinate(kost, field)
            if [x, y] in ValuableElement(field):
                break
        except:
            print('Неправильный инпут')

    x0, y0 = FindCoordinate('__', field)
    field[x][y] = '__'
    field[x0][y0] = f'{kost}'
    count_moves += 1

    Draw()
    if field == fieldWin:
        print('Победа', f'Кол-во ходов: {count_moves}', sep = '\n')
        break