'''from datetime import datetime, date, time
>>> # Using datetime.combine()
>>> d = date(2005, 7, 14)
>>> t = time(12, 30)
>>> datetime.combine(d, t)
datetime.datetime(2005, 7, 14, 12, 30)
>>> # Using datetime.now() or datetime.utcnow()
>>> datetime.now()
datetime.datetime(2007, 12, 6, 16, 29, 43, 79043)   # GMT +1
>>> datetime.utcnow()
datetime.datetime(2007, 12, 6, 15, 29, 43, 79060)
>>> # Using datetime.strptime()
>>> dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
>>> dt
datetime.datetime(2006, 11, 21, 16, 30)'''
import datetime

d = datetime.date(2005, 6, 30)
print(str(d))
t = datetime.time(10, 20, 5)
print(str(t))
dt = datetime.datetime(2000, 12, 12, 3, 3, 1, 1)

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

print(GetType(str(d)))
print(GetType(str(t)))
print(GetType(str(dt)))

print(SetType(str(d), 'datetime'))
print(SetType(str(t), 'datetime'))
print(SetType(str(dt), 'datetime'))