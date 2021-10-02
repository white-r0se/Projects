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
      'два':2,
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
    3:'тысячных'
}

def ToNum(numst):
    if ' и ' in numst:
        wholep, fractp = numst.split(' и ')
        return ToNum(wholep) + Fraction(fractp)
    elif ' ' in numst:
        numst = numst.split()
        return 10 * a2[numst[0]] + a1[numst[1]]
    else:
        if numst in a1:
            return(a1[numst])
        elif numst in tsat:
            return(tsat[numst])

def PrintNumb(s):
    if s == '':
        return ''
    s = str(s)
    p = []
    fr = ''
    lenfr = 0
    if '.' in s:
        s, fr = s.split('.')
        print(s, fr)
        lenfr = len(fr)
        fr = fr.replace('0', '')
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
        if len(s) == 3:
            p.append(ap3[int(s[-3])])
        if len(s) == 4:
            p.append(ap4[int(s[-4])])
    if fr == '':
        return(' '.join(p[::-1]))
    else:
        return(' '.join(p[::-1]) + ' и ' + PrintNumb(fr) + ' ' + lenfrac[lenfr])

def WordCalculator(line):
    if 'плюс' in line:
        newline = line.replace('плюс', '+')
        action = '+'
    elif 'минус' in line:
        newline = line.replace('минус', '-')
        action = '-'
    else:
        newline = line.replace('умножить', '*')
        action = '*'
    a, b = '', ''
    if '+' in newline:
        a = newline[0:newline.index('+')-1]
        b = newline[newline.index('+')+2:]
    elif '-' in newline:
        a = newline[0:newline.index('-')-1]
        b = newline[newline.index('-')+2:]
    else:
        a = newline[0:newline.index('*')-1]
        b = newline[newline.index('*')+2:]

    a, b = ToNum(a), ToNum(b)
    if action == '+':
        return(PrintNumb(a + b))
    elif action == '-':
        return(PrintNumb(a - b))
    elif action == '*':
        return(PrintNumb(a * b))

def Fraction(line):
    if ' тысячных' in line:
        newline = line.replace(' тысячных', '')
        return round(0.001 * ToNum(newline), 3)
    elif ' сотых' in line:
        newline = line.replace(' сотых', '')
        return round(0.01 * ToNum(newline), 3)
    elif ' десятых' in line:
        newline = line.replace(' десятых', '')
        return round(0.1 * ToNum(newline), 3)

print(WordCalculator('два и шесть сотых умножить пять'))