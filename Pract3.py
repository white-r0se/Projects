from os import SEEK_SET
import pickle
import csv
import copy

class Table:
    def __init__(self, object=None, rows=0, columns=0) -> None:
        if object == None:
            self.head = {i:'' for i in range(columns)}
            self.arr = [['' for i in range(columns)] for j in range(rows)]
        else:
            self.head = {i:object[0][i] for i in range(len(object[0]))}
            self.arr = [[object[j][i] for i in range(len(object[j]))] for j in range(1, len(object))]
    
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

    def get_rows_by_index(val1, … , copy_table=False): 
            '''получение новой таблицы
        из одной строки или из строк со значениями в первом столбце,
        совпадающими с переданными аргументами val1, … , valN. Функция либо
        копирует исходные данные, либо создает новое представление таблицы,
        работающее с исходным набором данных (copy_table=False), таким образом
        изменения, внесенные через это представления будут наблюдаться и в
        исходной таблице.'''

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
print('')
tabtxt.print_table()

