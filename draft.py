import random
import datetime

print(random.randrange(0, 6))
print(random.randrange(5, 10))
print(random.randrange(0, 11, 3))

def rand_date(date1, date2):
    d1, m1, y1 = map(int, date1.split('.'))
    d2, m2, y2 = map(int, date2.split('.'))
    return datetime.date(random.randrange(y1, y2+1), random.randrange(m1, m2+1), random.randrange(d1, d2+1))

print(rand_date('01.02.2022', '01.03.2022'))

