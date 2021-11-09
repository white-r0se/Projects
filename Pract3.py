import pickle
import csv
import copy
import datetime

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
    if '-' in x and not(':' in x):
        try:
            newx = datetime.date(*map(int, x.split('-')))
            return 'datatime'
        except TypeError:
            pass
    if ':' in x and not('-' in x):
        try:
            newx = datetime.time(*map(int, x.split(':')))
            return 'datatime'
        except TypeError:
            pass
    if '-' in x and ':' in x:
        try:
            arr = []
            date, time = x.split()
            arr += list(map(int, date.split('-')))
            arr += list(time.split(':'))
            for i in range(3, len(arr)):
                if i == 6:
                    arr[i] = float(arr[i])
                else:
                    arr[i] = int(i)
            newx = datetime.datetime(*arr)
            return 'datatime'
        except TypeError:
            pass
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
    elif type == 'datetime':
        if '-' in x and not(':' in x):
            return datetime.date(*map(int, x.split('-')))
    if ':' in x and not('-' in x):
        return datetime.time(*map(int, x.split(':')))
    if '-' in x and ':' in x:
        arr = []
        date, time = x.split()
        arr += list(map(int, date.split('-')))
        arr += list(time.split(':'))
        for i in range(3, len(arr)):
            if i == 6:
                arr[i] = float(arr[i])
            else:
                arr[i] = int(i)
        return datetime.datetime(*arr)

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
        d = {}
        for i in range(len(self.head)):
            if by_number == True:
                ind = i
            else:
                ind = self.head[i]
            d[ind] = GetType(self.arr[0][i])
            for j in range(len(self.arr)):
                if GetType(self.arr[j][i]) != d[ind]:
                    if (self.arr[j][i] == 'int' and d[ind] == 'float') or (self.arr[j][i] == 'float' and d[ind] == 'int'):
                        d[ind] = 'float'
                    else:
                        d[ind] = 'str' 
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
            self.dict_name = self.get_column_types(by_number=False)
            self.dict_num = self.get_column_types(by_number=True)
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

    def concat(table1, table2):
        if table1.head != table2.head:
            raise Exception('У таблиц разные столбцы!')
        newtab = Table(table1.transform_to_object())
        newtab.arr += table2.arr
        return newtab
    
    def split(self, row_number):
        if GetType(row_number) != 'int' or row_number < 0 or row_number > len(self.arr):
            raise IndexError('Неправильный номер строки!')
        newtab1 = Table(self.transform_to_object())
        newtab2 = Table(self.transform_to_object())
        while len(newtab1.arr) > row_number:
            newtab1.arr.pop(-1)
        for i in range(row_number):
            newtab2.arr.pop(0)
        return (newtab1, newtab2)

    def add(self, column1, column2, result_column):
        for i in [column1, column2, result_column]:
            if GetType(i) != 'int' or i < 0 or i > len(self.arr):
                raise IndexError('Неправильный номер строки!')
        type1, type2 = self.get_column_types()[column1], self.get_column_types()[column2]
        if type1 == 'str' or type2 == 'str' or type1 == 'datetime' or type2 == 'datetime':
            for i in range(len(self.arr)):
                self.arr[i][result_column] = str(self.arr[i][column1]) + str(self.arr[i][column2])
        else:
            for i in range(len(self.arr)):
                self.arr[i][result_column] = self.arr[i][column1] + self.arr[i][column2]

    def sub(self, column1, column2, result_column):
        for i in [column1, column2, result_column]:
            if GetType(i) != 'int' or i < 0 or i > len(self.arr):
                raise IndexError('Неправильный номер строки!')
        type1, type2 = self.get_column_types()[column1], self.get_column_types()[column2]
        if type1 == 'str' or type2 == 'str' or type1 == 'datetime' or type2 == 'datetime':
            for i in range(len(self.arr)):
                if str(self.arr[i][column2]) in str(self.arr[i][column1]):
                    self.arr[i][result_column] = str(self.arr[i][column1]).replace(str(self.arr[i][column2]), '')
                else:
                    raise TypeError('Ошибка вычитания str столбцов!')
        else:
            for i in range(len(self.arr)):
                self.arr[i][result_column] = self.arr[i][column1] - self.arr[i][column2]            

    def mul(self, column1, column2, result_column):
        for i in [column1, column2, result_column]:
            if GetType(i) != 'int' or i < 0 or i > len(self.arr):
                raise IndexError('Неправильный номер строки!')
        type1, type2 = self.get_column_types()[column1], self.get_column_types()[column2]
        if type1 == 'str' or type2 == 'str':
            raise TypeError('Нельзя использовать str столбцы!')
        elif  type1 == 'datetime' or type2 == 'datetime':
            raise TypeError('Нельзя использовать datetime столбцы!')
        else:
            for i in range(len(self.arr)):
                self.arr[i][result_column] = SetType(self.arr[i][column1], type1) * SetType(self.arr[i][column2], type2)

    def div(self, column1, column2, result_column):
        for i in [column1, column2, result_column]:
            if GetType(i) != 'int' or i < 0 or i > len(self.arr):
                raise IndexError('Неправильный номер строки!')
        type1, type2 = self.get_column_types()[column1], self.get_column_types()[column2]
        if type1 == 'str' or type2 == 'str':
            raise TypeError('Нельзя использовать str столбцы!')
        elif  type1 == 'datetime' or type2 == 'datetime':
            raise TypeError('Нельзя использовать datetime столбцы!')
        else:
            for i in range(len(self.arr)):
                self.arr[i][result_column] = SetType(self.arr[i][column1], type1) / SetType(self.arr[i][column2], type2)  

    def detect_type(self):
        self.dict_num = self.get_column_types(by_number=True)
        self.dict_name = self.get_column_types(by_number=False)

class TableCSV(Table):
    def load_table(self, *files, auto_detect_type=False):
        reader = []
        for i in files:
            reader.append(csv.reader(i, delimiter=';'))
        tablelists = []
        for i in range(len(reader)):
            tablelists.append(list(reader[i]))
        self.arr = []
        for i in range(len(tablelists)):
            self.arr += tablelists[i][1:]
        for i in range(len(tablelists[0][0])):
            self.head[i] = tablelists[0][0][i]
        if auto_detect_type:
            self.detect_type()

    def save_table(self, name='Table.csv', maxrows=None):
        if maxrows == None:
            with open(name, 'w', newline='') as newfile:
                writer = csv.writer(newfile, delimiter=';')
                writer.writerows(self.transform_to_object())
        else:
            if GetType(maxrows) != 'int':
                raise ValueError('max_rows должен быть int!')
            object_table = self.transform_to_object()
            head_table = object_table.pop(0)
            index = 0
            while True:
                newname = name.replace('.csv', f'{index}.csv')
                with open(newname, 'w', newline='') as newfile:
                    writer = csv.writer(newfile, delimiter=';')
                    writer.writerow(head_table)
                    for i in range(maxrows):
                        if object_table != []:
                            writer.writerow(object_table.pop(0))
                if object_table == []:
                    break
                index += 1
            
class TablePickle(Table):
    def save_table(self, name='Table.pickle', maxrows=None):
        if maxrows == None:
            with open(name, 'wb') as newfile:
                pickle.dump((self.head, self.arr), newfile)
        else:
            if GetType(maxrows) != 'int':
                raise ValueError('max_rows должен быть int!')
            index = 0
            while True:
                newname = name.replace('.pickle', f'{index}.pickle')
                with open(newname, 'wb') as newfile:
                    arr = []
                    for i in range(maxrows):
                        if self.arr != []:
                            arr.append(self.arr.pop(0))
                    pickle.dump((self.head, arr), newfile)
                if self.arr == []:
                    break
                index += 1
                            
    def load_table(self, *files, auto_detect_type=False):
        self.head, self.arr = pickle.load(files[0])
        for i in range(len(files)-1):
            head, arr = pickle.load(files[i+1])
            self.arr += arr
        if auto_detect_type:
            self.detect_type()
            

class TableTXT(Table):
    def save_table(self, name='Table.txt'):
        with open(name, 'w') as newfile:
            newfile.write(f'{len(self.head)} ')
            dic = self.head
            print(';'.join(list(dic.values())), file=newfile)
            for i in self.arr:
                print(';'.join(i), file=newfile)

    def load_table(self, file, auto_detect_type=False):
        elem, fordict = file.readline().split()
        fordict = fordict.split(';')
        for i in range(int(elem)):
            self.head[i] = fordict[i]
        lines = [line.rstrip() for line in file]
        for i in range(len(lines)):
            self.arr.append(list(lines[i].split(';')))
        if auto_detect_type:
            self.detect_type()


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
print('test .getvalue(s).....')
print(tabtxt.get_values('Age'))
print(tabtxt.get_value('City'))
print('\n')
print('test set_value(s).....')
tabtxt.set_values([16, 27, 80], column='Name')
tabtxt.set_value(18, column='Age')
tabtxt.print_table()
print('\n')
print('test load_table form 2 files.....')
f1 = open('file1.csv', 'r')
f2 = open('file2.csv', 'r')
tab1_2 = TableCSV()
tab1_2.load_table(f1, f2)
f1.close()
f2.close()
tab1_2.print_table()
tab1_2.save_table('Table_limit.csv', maxrows=3)
print('\n')
print('test save_table.....')
tab3.save_table('Table_limit.pickle', maxrows=2)
tab4 = TablePickle()
tab4.load_table(open('Table_limit0.pickle', 'rb'), open('Table_limit1.pickle', 'rb'))
tab4.print_table()
print('\n')
tab5 = TableCSV()
file3 = open('file3.csv', 'r')
tab5.load_table(file3)
tab4_5 = Table.concat(tab4, tab5)
print('test concat.....')
tab4_5.print_table()
print('\n')
print('test split.....')
tab4_5_1, tab4_5_2 = tab4_5.split(2)
tab4_5_1.print_table()
print()
tab4_5_2.print_table()
print('\n')
print('test add.....')
tab4_5_2.add(0, 1, 2)
tab4_5_2.print_table()
print()
print('test sub.....')
tab4_5_2.sub(2, 1, 2)
tab4_5_2.print_table()
print()
tab4_5_2.set_values([100, 200, 300], column='Name')
tab4_5_2.print_table()
tab4_5_2.div(0, 1, 2)
tab4_5_2.print_table()
print('\n')
print('test datetime....')
d = datetime.date(2005, 6, 30)
t = datetime.time(10, 20, 5)
dt = datetime.datetime(2000, 12, 12, 3, 3, 1, 1)
tab4_5_2.set_values([d, t, dt], column=2)
tab4_5_2.print_table()
print(tab4_5_2.get_column_types(by_number=False))