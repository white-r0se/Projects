def f1(*args):
    '''retueuwaewa'''
    return args

def f2(**kwargs):

    return kwargs

print(f1(1, 2, 3))
print(f1(*[1, 2,3 ]))

print(f2(a =2, b= 3))


print(f2(**{'a':{'c':21}, 'b':3}))