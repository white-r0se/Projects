#2
line = input()
count = 0
includes = []
first, last = -1, -1
if '*' not in line:
    print('нет символа')
else:
    for i in range(len(line)):
        if line[i] == '*':
            count += 1
            includes.append(i)
            if first == -1:
                first = i
            last = i
    if count == 1:
        print(includes[0])
    else:
        print(includes[0], includes[1], includes[-1])
        newline = list(line)
        newline.pop(first)
        newline.pop(last-1)
        print(''.join(newline))



#3
line = input()
line = ' '.join(line.split())
print(line)
line = line.swapcase()
print(line)
print(len(line.split()))


#5
a1 = {1:'один',
      2:'два',
      3:'три',
      4:'четыре',
      5:'пять',
      6:'шесть',
      7:'семь',
      8:'восемь',
      9:'девять',
      0:''}
     
a2 = {2:'двадцать',
      3:'тридцать',
      4:'сорок',
      5:'пятьдесят',
      6:'шестьдесят',
      7:'семьдесят',
      8:'восемьдесят',
      9:'девяносто'}
     
a3 = {1:'сто',
      2:'двести',
      3:'триста',
      4:'четыреста',
      5:'пятьсот',
      6:'шестьсот',
      7:'семьсот',
      8:'восемьсот',
      9:'девятьсот'}
     
tsat = {10:'десять',
      11:'одиннадцать',
      12:'двенадцать',
      13:'тринадцать',
      14:'четырнадцать',
      15:'пятнадцать',
      16:'шестнадцать',
      17:'семнадцать',
      18:'восемнадцать',
      19:'девятнадцать'}
s = input()
p = []
if len(s) > 1:
    if 9 < int(s[-2:]) < 20:
        p.append(tsat[int(s[-2:])])
    elif int(s[-2:]) > 19:
        p.append(a1[int(s[-1])])
        p.append(a2[int(s[-2])])
    else:
        if int(s[-1]) > 0:
            p.append(a1[int(s[-1])])
        else:
            p.append('ноль')
    if len(s) == 3:
        p.append(a3[int(s[-3])])
    print(' '.join(p[::-1]))
    p.clear()


#6
result = 0
line = input()
newline = line.replace('-', '+')
arr_numbers = newline.split('+')
for i in range(len(arr_numbers)):
    arr_numbers[i] = int(arr_numbers[i])
arr_destv = []
for i in range(len(line)):
    if line[i] == '+' or line[i] == '-':
        arr_destv.append(line[i])
result += arr_numbers[0]
for i in range(len(arr_destv)):
    if arr_destv[i] == '+':
        result += arr_numbers[i+1]
    else:
        result -= arr_numbers[i+1]
print(result)



#7
line1 = input()
line2 = input()
if len(line1) > len(line2):
    print(f'Первая длиннее на {len(line1) - len(line2)}')
else:
    print(f'Вторая длиннее на {len(line2) - len(line1)}')
    
if line > line2: print('Первая стоит раньше в лексокограф. порядке')
else: print('Вторая стоит раньше в лексокограф. порядке')
result = line1 + '\\n' + line2
print(result)


 #8
arr = input().split()
arr[0], arr[2] = int(arr[0]), int(arr[2])
if arr[1] == '+':
    print(f'a + b = {arr[0]} + {arr[2]} = {arr[0] + arr[2]}')
elif arr[1] == '-':
    print(f'a - b = {arr[0]} - {arr[2]} = {arr[0] - arr[2]}')
elif arr[1] == '*':
    print(f'a * b = {arr[0]} * {arr[2]} = {arr[0] * arr[2]}')
elif arr[1] == '/':
    print(f'a / b = {arr[0]} / {arr[2]} = {arr[0] / arr[2]}')
elif arr[1] == '**':
    print(f'a ** b = {arr[0]} ** {arr[2]} = {arr[0] ** arr[2]}')
elif arr[1] == '%':
    print(f'a % b = {arr[0]} % {arr[2]} = {arr[0] % arr[2]}')



#1
import math
a = int(input())
b = int(input())
print('x   |  sinx')
while a < b:
    print(f'{a:.2f}   {math.sin(a):.2f}')
    a += 0.1



#2
arr = []
while True:
    line = input()
    if line == '0':
        break
    arr.append(int(line))
summ = 0
for i in arr:
    summ += i
print(len(line), max(line), min(line), summ, summ / len(arr))

#3
minn = 10000000
while True:
    line = input()
    if line == '.':
        break
    num = int(line)
    if num > 0 and num < minn:
        minn = num
print(minn)