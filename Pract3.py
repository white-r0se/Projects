import pickle
import csv
import copy

def GetType(x):
    try:
        newx = int(x)
        if str(newx) == x:
            return 'int'
        elif newx == x:
            return 'int'
    except ValueError:
        pass
    try:
        newx = float(x)
        return 'float'
    except ValueError:
        pass
    if x == 'True' or x == 'False':
        return 'bool'
    return 'str'

def SetType(x, type):
    if type == 'bool':
        return bool(x)
    elif type == 'int':
        return int(x)
    elif type == 'float':
        return float(x)
    elif type == 'str':
        return str(x)

class Table:
    def __init__(self, object=None, rows=0, columns=0) -> None:
        if object == None:
            self.head = {i:'' for i in range(columns)}
            self.arr = [['' for i in range(columns)] for j in range(rows)]
            self.dict_num = {}
            self.dict_name = {}
        else:
            self.head = {i:object[0][i] for i in range(len(object[0]))}
            self.arr = [[object[j][i] for i in range(len(object[j]))] for j in range(1, len(object))]
            self.dict_num = {}
            self.dict_name = {}
    
    def print_table(self):
        for i in range(len(self.head)):
            print(self.head[i], end='  ')
        print()
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                print(self.arr[i][j], end='  ')
            print()

    def transform_to_object(self):
        return [list(self.head.values())] + self.arr

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        if start < 0 or start > len(self.arr) or stop < 0 or stop > len(self.arr):
            raise IndexError('Неправильный интервал строк!')
        if stop == None:
            stop = start + 1
        if copy_table == True:
            newtable = self
            newtable.arr = self.arr[start:stop]
            return newtable
        else:
            newtable = copy.deepcopy(self)
            newtable.arr = copy.deepcopy(self.arr[start:stop])
            return newtable

    def get_rows_by_index(self, *values, copy_table=False): 
        if copy_table == True:
            newtable = self
            rows = []
            for i in values:
                for j in self.arr:
                    if i == j[0]:
                        rows.append(j)
                        break
                    if j == self.arr[-1]:
                        raise ValueError('Неправильное значение!')
            newtable.arr = rows
            return newtable
        else:
            newtable = copy.deepcopy(self)
            rows = []
            for i in values:
                for j in self.arr:
                    if i == j[0]:
                        rows.append(copy.deepcopy(j))
                        break
                    if j == self.arr[-1]:
                        raise ValueError('Неправильное значение!')
            newtable.arr = rows
            return newtable

    def get_column_types(self, by_number=True):
        if by_number != True and by_number != False:
            raise TypeError('by_number принимает только True и False!')
        if by_number == True and self.dict_num != {}:
            return self.dict_num
        elif by_number == False and self.dict_name != {}:
            return self.dict_name
        d = {}
        for i in range(len(self.head)):
            if by_number == True:
                ind = i
            else:
                ind = self.head[i]
            d[ind] = GetType(self.arr[0][i])
        return d
    
    def set_column_types(self, types_dict, by_number=True):
        if by_number != True and by_number != False:
            raise TypeError('by_number принимает только True и False!')
        self.dict_num = self.get_column_types(by_number=True)
        self.dict_name = self.get_column_types(by_number=False)
        if by_number == True:
            c = 0
            for i in self.dict_num:
                self.dict_num[i] = types_dict.pop(c)
                c += 1
            c = 0
            for i in self.dict_name:
                self.dict_name[i] = self.dict_num[c]
                c += 1
        else:
            c = 0
            copy_types_dict = copy.deepcopy(types_dict)
            for i in types_dict:
                self.dict_name[i] = copy_types_dict.pop(i)
                self.dict_num[c] = self.dict_name[i]
                c += 1
        
    def get_values(self, column=0):
        self.dict_num = self.get_column_types(by_number=True)
        self.dict_name = self.get_column_types(by_number=False)
        arr = []
        if GetType(column) == 'int':
            if column < 0 or column > len(self.dict_num)-1:
                raise ValueError('Неправильный номер столбца!')
            for i in self.arr:
                arr.append(SetType(i[column], self.dict_num[column]))
        else:
            if not(column in self.dict_name):
                raise IndexError('Столбец с таким именем не найден!')
            c = 0
            for i in self.dict_name:
                if column == i:
                    break
                c += 1
            for i in self.arr:
                arr.append(SetType(i[c], self.dict_name[column]))
        return arr
            
    def get_value(self, column=0):
        return self.get_values(column)[0]

    def set_values(self, values, column=0):
        if GetType(column) == 'int':
            if column < 0 or column > len(self.dict_num)-1:
                raise ValueError('Неправильный номер столбца!')
            index = column
        else:
            if not(column in self.dict_name):
                raise IndexError('Столбец с таким именем не найден!')
            index = 0
            for i in self.dict_name:
                if column == i:
                    break
                index += 1
        for i in range(len(self.arr)):
            self.arr[i][index] = SetType(values[i], self.dict_num[index])
        
    def set_value(self, value, column=0):
        if GetType(column) == 'int':
            if column < 0 or column > len(self.dict_num)-1:
                raise ValueError('Неправильный номер столбца!')
            index = column
        else:
            if not(column in self.dict_name):
                raise IndexError('Столбец с таким именем не найден!')
            index = 0
            for i in self.dict_name:
                if column == i:
                    break
                index += 1
        self.arr[0][index] = SetType(value, self.dict_num[index])

class TableCSV(Table):
    def load_table(self, file):
        reader = csv.reader(file, delimiter=';')
        tablelist = list(reader)
        self.arr = tablelist[1:]
        for i in range(len(tablelist[0])):
            self.head[i] = tablelist[0][i]

    def save_table(self, name='Table.csv'):
        with open(name, 'w', newline='') as newfile:
            writer = csv.writer(newfile, delimiter=';')
            writer.writerows(self.transform_to_object())

class TablePickle(Table):
    def save_table(self, name='Table.pickle'):
        with open(name, 'wb') as newfile:
            pickle.dump((self.head, self.arr), newfile)

    def load_table(self, file):
        self.head, self.arr = pickle.load(file)

class TableTXT(Table):
    def save_table(self, name='Table.txt'):
        with open(name, 'w') as newfile:
            newfile.write(f'{len(self.head)} ')
            dic = self.head
            print(';'.join(list(dic.values())), file=newfile)
            for i in self.arr:
                print(';'.join(i), file=newfile)

    def load_table(self, file):
        elem, fordict = file.readline().split()
        fordict = fordict.split(';')
        for i in range(int(elem)):
            self.head[i] = fordict[i]
        lines = [line.rstrip() for line in file]
        for i in range(len(lines)):
            self.arr.append(list(lines[i].split(';')))


with open('file1.csv', 'r') as File1:
    tab1 = TableCSV()
    tab1.load_table(File1)
    print('READ file1.csv.....')
    tab1.print_table()
    tab1.arr[1][1] = 28
    tab1.save_table('testsave.csv')
    print('\n')

with open('testsave.csv', 'r', newline='') as File2:
    tab2 = TableCSV()
    tab2.load_table(File2)
    print('READ testsave.csv.....')
    tab2.print_table()
    tab3 = TablePickle(tab2.transform_to_object())
    tab3.save_table()
    tabtxt = TableTXT(tab2.transform_to_object())
    tabtxt.save_table()
    print('\n')

with open('Table.pickle', 'rb') as File3:
    tab3 = TablePickle()
    tab3.load_table(File3)
    print('READ Table.pickle.....')
    tab3.print_table()
    print('\n')

with open('Table.txt', 'r') as FileTXT:
    tabtxt = TableTXT()
    tabtxt.load_table(FileTXT)
    print('READ Table.txt.....')
    tabtxt.print_table()
    print('\n')

print('COPY tabtxt.....')
copytable = tabtxt.get_rows_by_number(0, 2, copy_table=False)
copytable.arr[1][1] = '27' 
copytable.print_table()
print('--')
tabtxt.print_table()
print('\n')
print('COPY tabtxt by index.....')
copy2table = tabtxt.get_rows_by_index('Alexey', 'Al Pacino', copy_table=False)
copy2table.print_table()
copy2table.arr[1][1] = 82
print('--')
tabtxt.print_table()
print('\n')
print(tabtxt.get_column_types(by_number=False))
tabtxt.set_column_types({'Name':'bool'}, by_number=False)
print(tabtxt.get_column_types(by_number=True))
print('\n')
print(tabtxt.get_values('Age'))
print(tabtxt.get_value('City'))
print('\n')
tabtxt.set_values([16, 27, 80], column='Name')
tabtxt.set_value(18, column='Age')
tabtxt.print_table()
