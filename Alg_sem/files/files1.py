#1

with open('Alg_sem\\files_sem1.txt') as file1:
    lines = file1.readlines()
    maxlen = max(map(len, lines))
    minlen = min(map(len, lines))

minline = lines[list(map(len, lines)).index(minlen)]
maxlines = []

for line in lines:
    if len(line) == maxlen:    
        maxlines.append(line)

with open('Alg_sem\\output_file1.txt', 'w') as file1_1:
    print(f'Max len of lines: {maxlen}', file=file1_1)
    for line in maxlines:
        print(f'{line}', file=file1_1)
    print(f'Max len of lines: {minlen}', file=file1_1)
    print(f'{minline}', file=file1_1)


#2

with open('Alg_sem\\file2_sem1.txt', 'r+') as file2:
    lines = file2.readlines()

    namegood = input('Введите название товара:')
    for line in lines:
        if namegood in line:
            print(line)
            break
    else:
        print('Price is unknown, sorry :(')

    print(f'Chips:2$\nChebupizza:2$\nFries:0.7$', file=file2)

with open('Alg_sem\\file2_sem1.txt', 'r+') as file2:
    lines = file2.readlines()
    file2.seek(0)
    for line in lines:
        if line != 'Sprite:1$\n':
            file2.write(line)
    file2.truncate()
    
d = {}    
for line in lines:
    name, price = line.split(':')
    d[name] = price
sorted_tuples = sorted(d.items(), key=lambda item: item[1])
sorted_dict = {k: v for k, v in sorted_tuples}

with open('Alg_sem\\output_file2.txt', 'w', encoding='utf-8') as outfile:
    for el in sorted_dict:
        print(f'{el}:{sorted_dict[el]}', file=outfile, end='')

    i = 0
    for el in sorted_dict:
        if i == 0:
            print('Два самых дешевых:')
            print(f'{el}:{sorted_dict[el]}', end='')
        elif i == 1:
            print(f'{el}:{sorted_dict[el]}', end='')
            print('Два самых дорогих:')
        elif i>=len(sorted_dict)-2:
            print(f'{el}:{sorted_dict[el]}', end='')
        i += 1
        

#3
with open('Alg_sem\\file3_sem1.txt') as file3_1:
    lines1 = file3_1.readlines()

with open('Alg_sem\\file3_2_sem1.txt') as file3_2:
    lines2 = file3_2.readlines()

lines1 = list(map(int, lines1))
lines2 = list(map(int, lines2))

outlist = []

while 1:
    if lines1[0] >= lines2[0]:
        outlist.append(lines2.pop(0))
    else:
        outlist.append(lines1.pop(0))

    if len(lines1) == 0:
        outlist += lines2
        break
    elif len(lines2) == 0:
        outlist += lines1
        break

with open('Alg_sem\\output_file3.txt', 'w') as file3_3:
    for num in outlist:
        print(num, file=file3_3)

    
