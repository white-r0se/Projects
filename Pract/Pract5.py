from cProfile import label
from calendar import c
import math
import random
from matplotlib import pyplot as plt
import numpy as np

# matrix = [[0, 2, 0, 0, 0], [2, 0, 3, 0, 0], [0, 3, 0, 4, 1], [0, 0, 4, 0, 2], [0, 0, 1, 2, 0]]
# matrix = [[0, 3, 0, 0, 0, 4], [3, 0, 4, 8, 0, 0], [0, 4, 0, 40, 0, 1], [0, 8, 40, 0, 18, 10], [0, 0, 0, 18, 0, 2], [4, 0, 1, 10, 2, 0]]
matrix = [[0, 10, 12, 8, 9, 11], [21, 0, 7, 5, 21, 3], [13, 19, 0, 13, 4, 15], [15, 20, 14, 0, 10, 10], [7, 15, 9, 12, 0, 23], [16, 3, 11, 8, 17, 0]]
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
        if cur_ver == cache[-1]:
            all_roads.append(cur_time)
        return None
    if matrix[cur_ver] != [0]*n:
        for i in range(n):
            if matrix[cur_ver][i] != 0 and not(i in cache[1:]):
                Recursion_search(i, cur_time+matrix[cur_ver][i], cache+[i])

            
Recursion_search(0, 0, [0])
print('Полный перебор:', min(all_roads))    
        
# Nearest neigbour Algorithm 

roads = []
for start in range(n):
    nearest_neighbour_roads = []
    cur_ver = start
    cache = [start]
    count = 0
    while len(nearest_neighbour_roads) != n-1:
        if matrix[cur_ver] != [0]*n:
            try:
                min_road = min([matrix[cur_ver][i] for i in range(n) if (matrix[cur_ver][i] != 0 and not(i in cache))])
            except ValueError:
                # broken path
                nearest_neighbour_roads = [10000]
                break
            i = matrix[cur_ver].index(min_road)
            if not(i in cache):
                nearest_neighbour_roads.append(matrix[cur_ver][i])
                cur_ver = i
                cache.append(cur_ver)
        count += 1
        if count > 100:
            # broken path
            nearest_neighbour_roads = [10000]
            break
    roads.append(sum(nearest_neighbour_roads))

print('Алгоритм ближайшего соседа:', min(roads))

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

for start in range(n):
    for i in range(20):
        Ant(start, 0, [start])
print('Ant Algorithm:', min_road)

# метод включения близж города

roads = []
for start in range(n): 
    nearest_neighbour_roads = []
    nearest_neighbour_vers = [0]
    cache_vers = [0]

    count = 0
    while len(nearest_neighbour_roads) != n-1:
        challenger_vers = []
        challenger_roads = []
        for cur_ver in [cache_vers[-1]] + [cache_vers[0]]:
            if matrix[cur_ver] != [0]*n:
                
                vers = [i for i in range(len(matrix[cur_ver])) if matrix[cur_ver][i] != 0]
                for ver in vers:
                    if ver in cache_vers:
                        pass
                    else:
                        challenger_roads.append(min([matrix[cur_ver][i] for i in range(n) if (matrix[cur_ver][i] != 0 and not(i in cache_vers))]))
                        challenger_vers.append(matrix[cur_ver].index(challenger_roads[-1]))

        i = challenger_roads.index(min(challenger_roads))        
        nearest_neighbour_roads.append(challenger_roads[i])
        cache_vers.append(challenger_vers[i])

        count += 1
        if count > 100:
            # broken path
            nearest_neighbour_roads = [10000]
            break

    roads.append(sum(nearest_neighbour_roads))

print('Алгоритм включения ближайшего соседа:', min(roads))

# dynamic algorithm

def findCheapest(i, mask):
    if dp[i][mask] != inf:
        return dp[i][mask] 
    for j in range(n):
        if l[i][j] != 0 and ((mask >> j) & 1 == 1):  
            dp[i][mask] = min(dp[i][mask], findCheapest(j, mask - 2**j) + l[i][j])
    return dp[i][mask]

def findWay():
    i = 0
    mask = 2**n - 1
    way.append(0)
    while mask != 0:
        for j in range(n):
            if l[i][j] != 0 and ((mask >> j) & 1 == 1) and (dp[i][mask] == dp[j][mask - 2**j] + l[i][j]): 
                way.append(j)
                i = j
                mask = mask - 2**j
                continue
    print(way)

inf = math.inf
# n = 5
dp = [[inf] * (2**n) for i in range(n)]
# l =[[0,5,9,0,0],
#     [5,0,0,7,3],
#     [9,0,0,4,5],
#     [0,7,4,0,6],
#     [0,3,5,6,0]]
l = matrix
way = []
dp[0][0] = 0
ans = findCheapest(0, 2**n - 1)
findWay()

