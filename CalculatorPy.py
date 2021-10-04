ap1 = {1:'один',
      2:'два',
      3:'три',
      4:'четыре',
      5:'пять',
      6:'шесть',
      7:'семь',
      8:'восемь',
      9:'девять',
      0:''}
     
ap2 = {2:'двадцать',
      3:'тридцать',
      4:'сорок',
      5:'пятьдесят',
      6:'шестьдесят',
      7:'семьдесят',
      8:'восемьдесят',
      9:'девяносто'}
     
ap3 = {1:'сто',
      2:'двести',
      3:'триста',
      4:'четыреста',
      5:'пятьсот',
      6:'шестьсот',
      7:'семьсот',
      8:'восемьсот',
      9:'девятьсот'}

ap4 = {1:'одна тысяча',
    2:'два тысячи',
    3:'три тысячи',
    4:'четрые тысячи',
    5:'пять тысяч',
    6:'шесть тысяч',
    7:'семь тысяч',
    8:'восемь тысяч',
    9:'девять тысяч'}

tsatp = {10:'десять',
      11:'одиннадцать',
      12:'двенадцать',
      13:'тринадцать',
      14:'четырнадцать',
      15:'пятнадцать',
      16:'шестнадцать',
      17:'семнадцать',
      18:'восемнадцать',
      19:'девятнадцать'}

a1 = {'один':1,
      'одна':1,
      'два':2,
      'две':2,
      'три':3,
      'четыре':4,
      'пять':5,
      'шесть':6,
      'семь':7,
      'восемь':8,
      'девять':9
     }
     
a2 = {'двадцать':2,
      'тридцать':3,
      'сорок':4,
      'пятьдесят':5,
      'шестьдесят':6,
      'семьдесят':7,
      'восемьдесят':8,
      'девяносто':9
     }

a3 = {'сто':1,
      'двести':2,
      'триста':3,
      'четыреста':4,
      'пятьсот':5,
      'шестьсот':6,
      'семьсот':7,
      'восемьсот':8,
      'девятьсот':9}

tsat = {'десять':10,
      'одиннадцать':11,
      'двенадцать':12,
      'тринадцать':13,
      'четырнадцать':14,
      'пятнадцать':15,
      'шестнадцать':16,
      'семнадцать':17,
      'восемнадцать':18,
      'девятнадцать':19
       }

lenfrac = {
    1:'десятых',
    2:'сотых',
    3:'тысячных',
    4:'десятитысячных',
    5:'стотысячных',
    6:'миллионных'
}

def ToNum(numst):
    print(numst)
    if ' и ' in numst:
        wholep, fractp = numst.split(' и ')
        return ToNum(wholep) + Fraction(fractp)
    elif lenfrac[1] in numst or lenfrac[2] in numst or lenfrac[3] in numst or lenfrac[4] in numst or lenfrac[5] in numst or lenfrac[6] in numst:
        fractp = numst
        return Fraction(fractp)
    elif ' ' in numst:
        numst = numst.split()
        return 10 * a2[numst[0]] + a1[numst[1]]
    else:
        if numst in a1:
            return(a1[numst])
        elif numst in tsat:
            return(tsat[numst])
        elif numst in a2:
            return(a2[numst])
        elif numst in a3:
            return(a3[numst])

def CheckFracPeriod(numfr):
    # numfr = f'{numfr:.11f}'
    print(numfr)
    for i in range(4, len(numfr)):
        if numfr[i] == numfr[i-1] == numfr[i-2] == numfr[i-3] == numfr[i-4] and numfr[i] != '0':
            return [numfr[i], i-4]
        elif [numfr[i], numfr[i-1]] == [numfr[i-2], numfr[i-3]] == [numfr[i-4], numfr[i-5]] != ['0', '0'] and i >= 5:
            return [f'{numfr[i-1]}{numfr[i]}', i-5]
        elif [numfr[i], numfr[i-1], numfr[i-2]] == [numfr[i-3], numfr[i-4], numfr[i-5]] == [numfr[i-6], numfr[i-7], numfr[i-8]] != ['0', '0', '0'] and i >= 8:
            return [f'{numfr[i-2]}{numfr[i-1]}{numfr[i]}', i-8]
        elif [numfr[i], numfr[i-1], numfr[i-2], numfr[i-3]] == [numfr[i-4], numfr[i-5], numfr[i-6], numfr[i-7]] == [numfr[i-8], numfr[i-9], numfr[i-10], numfr[i-11]] != ['0', '0', '0', '0'] and i>=11:
            return [f'{numfr[i]-3}{numfr[i-2]}{numfr[i-1]}{numfr[i]}', i-11]

def PrintNumb(s):
    if s == '':
        return ''
    print(s)
    if s == int(s):
        s = int(s)
    s = str(s)
    p = []
    fr = ''
    frperiod = False
    lenfr = 0
    if '.' in s:
        s, fr = s.split('.')
        lenfr = len(fr)
        if CheckFracPeriod(fr) != None:
            frperiod = True
            per, index = CheckFracPeriod(fr)
            beforper = fr[:index]
            lenfr = len(beforper)
        else:
            s = float(f'{s}.{fr}')
            s = round(float(s), 6)
            s = str(s)
            s, fr = s.split('.')
            print('New f:', fr)
            lenfr = len(fr)
            fr = list(fr)
            while fr[len(fr)-1] == 0:
                del fr[len(fr-1)]
            fr = ''.join(fr)
    if len(s) >= 1:  
        if 9 < int(s[-2:]) < 20:
            p.append(tsatp[int(s[-2:])])
        elif int(s[-2:]) > 19:
            p.append(ap1[int(s[-1])])
            p.append(ap2[int(s[-2])])
        else:
            if int(s[-1]) > 0:
                p.append(ap1[int(s[-1])])
            else:
                p.append('ноль')
        if len(s) >= 3 and int(s[-3]) != 0:
            p.append(ap3[int(s[-3])])
        if len(s) >= 4 and int(s[-4]) != 0:
            p.append(ap4[int(s[-4])])
        if len(s) == 5 or len(s) == 6:
            if int(s[-4]) == 1 and int(s[-5]) != 1:
                p.append('тысяча')
            elif int(s[-4]) == 2 and int(s[-5]) != 1:
                p.append('тысячи')
            elif int(s[-4]) == 3 and int(s[-5]) != 1:
                p.append('тысячи')
            elif int(s[-4]) == 4 and int(s[-5]) != 1:
                p.append('тысячти')
            else:
                p.append('тысяч')
        
            num5 = int(s[-5:-3])
            print('num5', num5)
            if 9 < num5 < 20:
                p.append(tsatp[num5])
            elif num5 > 19:
                p.append(ap1[int(s[-4])])
                p.append(ap2[int(s[-5])])
            if len(s) == 6 and s[-6] != '0':
                p.append(ap3[int(s[-6])])
    if fr == '':
        return(' '.join(p[::-1]))
    elif frperiod == True:
        if lenfr != 0:
            return(' '.join(p[::-1]) + ' и ' + PrintNumb(beforper) + lenfrac[lenfr] + ' и ' + PrintNumb(per) + ' в периоде')
        else:
            return(' '.join(p[::-1]) + ' и ' + PrintNumb(per) + ' в периоде')
    else:
        return(' '.join(p[::-1]) + ' и ' + PrintNumb(fr) + ' ' + lenfrac[lenfr])

def WordCalculator(line):
    if 'плюс' in line:
        newline = line.replace('плюс', '+')
        action = '+'
    elif 'минус' in line:
        newline = line.replace(' минус', '-')
        action = '-'
    elif 'умножить' in line:
        newline = line.replace(' умножить на ', '*')
        action = '*'
    elif 'разделить на' in line:
        newline = line.replace(' разделить на ', '/')
        action = '/'
    elif ' остаток от деления на ' in line:
        newline = line.replace(' остаток от деления на ', '%')
        action = '%'
    a, b = '', ''
    if '+' in newline:
        a, b = newline.split('+')
    elif '-' in newline:
        a, b = newline.split('-')
    elif '*' in newline:
        a, b = newline.split('*')
    elif '/' in newline:
        a, b = newline.split('/')
    elif '%' in newline:
        a, b = newline.split('%')
    a, b = ToNum(a), ToNum(b)
    if action == '+':
        return(PrintNumb(a + b))
    elif action == '-':
        return(PrintNumb(a - b))
    elif action == '*':
        return(PrintNumb(a * b))
    elif action == '/':
        return(PrintNumb(a / b))
    elif action == '%':
        return(PrintNumb(a % b))

def Fraction(line):
    if ' миллионных' in line:
        newline = line.replace(' миллионных', '')
        return round(0.000001 * ToNum(newline), 6)
    elif ' стотысячных' in line:
        newline = line.replace(' стотысячных', '')
        return round(0.00001 * ToNum(newline), 6)
    elif ' десятитысячных' in line:
        newline = line.replace(' десятитысячных', '')
        return round(0.0001 * ToNum(newline), 6)
    elif ' тысячных' in line:
        newline = line.replace(' тысячных', '')
        return round(0.001 * ToNum(newline), 6)
    elif ' тысячная' in line:
        newline = line.replace(' тысячная', '')
        return round(0.001 * ToNum(newline), 6)
    elif ' сотых' in line:
        newline = line.replace(' сотых', '')
        return round(0.01 * ToNum(newline), 6)
    elif ' десятых' in line:
        newline = line.replace(' десятых', '')
        return round(0.1 * ToNum(newline), 6)

print(WordCalculator('девятнадцать и восемьдесят две сотых разделить на девяносто девять'))
# print(PrintNumb())
