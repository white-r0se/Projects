from cProfile import label
from calendar import c
import math
import random
from matplotlib import pyplot as plt
import numpy as np

# matrix = [[0, 2, 0, 0, 0], [2, 0, 3, 0, 0], [0, 3, 0, 4, 1], [0, 0, 4, 0, 2], [0, 0, 1, 2, 0]]
matrix = [[0, 3, 0, 0, 0, 1], [3, 0, 4, 0, 0, 0], [0, 4, 0, 1, 0, 0], [0, 0, 1, 0, 10, 3], [0, 0, 0, 10, 0, 2], [1, 0, 0, 3, 2, 0]]
n = len(matrix)

# DRAW

def Polygon(sides, radius=1, rotation=0, translation=None):
    one_segment = math.pi * 2 / sides
    points = [
        (math.sin(one_segment * i + rotation) * radius,
         math.cos(one_segment * i + rotation) * radius)
        for i in range(sides)]
    if translation:
        points = [[sum(pair) for pair in zip(point, translation)]
                  for point in points]
    return points

x, y = [], []
for point in Polygon(n):
    px, py = point
    x.append(px)
    y.append(py)
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.grid()
plt.rcParams["figure.autolayout"] = True
for i in range(n):
    for j in range(i, n):
        if matrix[i][j] != 0:
            plt.plot([x[i], x[j]], [y[i], y[j]], marker="o", markersize=2, markeredgecolor="red")
            plt.text((x[i]+x[j])/2, (y[i]+y[j])/2, f'{matrix[i][j]}')
plt.show()

# all permutations 

all_roads = []

def Recursion_search(cur_ver, cur_time, cache):
    global n
    global all_roads
    if len(cache) == n:
        all_roads.append(cur_time)
        return None
    if matrix[cur_ver] != [0]*n:
        for i in range(n):
            if matrix[cur_ver][i] != 0 and not(i in cache):
                Recursion_search(i, cur_time+matrix[cur_ver][i], cache+[i])
            
Recursion_search(0, 0, [0])
print('Кратчайший путь (с помощью полного перебора):', min(all_roads))    
        
# Nearest neigbour Algorithm 

nearest_neighbour_roads = []
cur_ver = 0
cache = [0]

count = 0
while len(nearest_neighbour_roads) != n-1:
    if matrix[cur_ver] != [0]*n:
        min_road = min([matrix[cur_ver][i] for i in range(n) if (matrix[cur_ver][i] != 0 and not(i in cache))])
        i = matrix[cur_ver].index(min_road)
        if not(i in cache):
            nearest_neighbour_roads.append(matrix[cur_ver][i])
            cur_ver = i
            cache.append(cur_ver)
    count += 1
    if count > 100:
        print('Sorry')
        break

print('Кратчайший путь (с помощью алгоритма ближайшего соседа):', sum(nearest_neighbour_roads))

#     No ant colony optimization?
#⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
#⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
#⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
#⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
#⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
#⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# Ant colony Algorithm
min_road = 1000
pheromone_matrix = [[0 for i in range(n)] for j in range(n)]
a, b = 1, 1 # параметры, определяющие важность веса ребра и уровень феромона
k = 1.5 # параметр, определяющий интенсивность следа феромона
evaporation_time = 3/5 # коэффицент скорости испарения феромона
 
def Pheromone_update(cache) -> None:
    global pheromone_matrix
    for i in range(n):
        for j in range(n):
            if pheromone_matrix[i][j] != 0:
                pheromone_matrix[i][j] *= evaporation_time

    for j in range(1, len(cache)):
        ver1, ver2 = cache[j-1], cache[j]
        pheromone_matrix[ver1][ver2] = k/matrix[ver1][ver2]


def Ant(cur_ver, cur_time, cache):
    if len(cache) == n:
        global min_road
        min_road = min(min_road, cur_time)
        Pheromone_update(cache)
        return None
    if matrix[cur_ver] != [0]*n:
        p = [0]*n
        for i in range(n):
            if matrix[cur_ver][i] != 0 and not(i in cache):
                p[i] = (pheromone_matrix[cur_ver][i]**a + 1/matrix[cur_ver][i]**b) / sum([pheromone_matrix[cur_ver][l]**a + 1/matrix[cur_ver][l]**b for l in range(n) if matrix[cur_ver][l] != 0])
        if p == [0]*n:
            return None
        new_ver = random.choices([i for i in range(n)], weights=p)[0]
        Ant(new_ver, cur_time + matrix[cur_ver][new_ver], cache + [new_ver])

for i in range(10):
    Ant(0, 0, [0])
print(min_road)

# 