import math
import random
from matplotlib import pyplot as plt

matrix = [[0, 10, 12, 8, 9, 11], [21, 0, 7, 5, 21, 3], [13, 19, 0, 13, 4, 15], [15, 20, 14, 0, 10, 10], [7, 15, 9, 12, 0, 23], [16, 3, 11, 8, 17, 0]]
n = len(matrix)
inf = math.inf

# Draw

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

# All permutations 

roads = []

def Recursion_search(cur_ver, cur_time, cache):
    global n
    global roads

    if len(cache) == n+1:
        if cur_ver == cache[0]:
            roads.append(cur_time)
        return None
    if matrix[cur_ver] != [0]*n:
        for i in range(n):
            if matrix[cur_ver][i] != 0 and (not(i in cache) or (len(cache) == n and i == cache[0])):
                Recursion_search(i, cur_time + matrix[cur_ver][i], cache + [i])

Recursion_search(0, 0, [0])
print('All permutations:', min(roads))    

# Nearest neigbour Algorithm 

nearest_neighbour_roads = []
cur_ver = 0
cache = [0]
count = 0

while len(cache) != n+1:
    if matrix[cur_ver] != [0]*n:
        try:
            min_road = min([matrix[cur_ver][i] for i in range(n) if matrix[cur_ver][i] != 0 and (not(i in cache) or (len(cache) == n and i == cache[0]))])
        except ValueError:
            # broken path
            nearest_neighbour_roads = [inf]
            break
        i = matrix[cur_ver].index(min_road)
        if (not(i in cache) or (len(cache) == n and i == cache[0])):
            nearest_neighbour_roads.append(matrix[cur_ver][i])
            cur_ver = i
            cache.append(cur_ver)
    count += 1
    if count > 100:
        # broken path
        nearest_neighbour_roads = [inf]
        break

print('Nearest neigbour Algorithm:', sum(nearest_neighbour_roads))

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
a, b = 1, 1 # parameters that determine the importance of edge weight and pheromone level
k = 1.5 # parameter that determines the intensity of the pheromone trail
evaporation_time = 3/5 # pheromone evaporation rate coefficient
iter_num = 30 # number of iterations (number of ants)
 
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
    if len(cache) == n+1:
        global min_road
        min_road = min(min_road, cur_time)
        Pheromone_update(cache)
        return None
    if matrix[cur_ver] != [0]*n:
        p = [0]*n
        for i in range(n):
            if matrix[cur_ver][i] != 0 and (not(i in cache) or (len(cache) == n and i == cache[0])):
                p[i] = (pheromone_matrix[cur_ver][i]**a + 1/matrix[cur_ver][i]**b) / sum([pheromone_matrix[cur_ver][l]**a + 1/matrix[cur_ver][l]**b for l in range(n) if matrix[cur_ver][l] != 0])
        if p == [0]*n:
            return None
        new_ver = random.choices([i for i in range(n)], weights=p)[0]
        Ant(new_ver, cur_time + matrix[cur_ver][new_ver], cache + [new_ver])

for i in range(iter_num):
    Ant(0, 0, [0])
print('Ant Algorithm:', min_road)

# Сlosest city inclusion method

nearest_neighbour_roads = []
cache = [0]
count = 0

while len(cache) != n:
    challenger_vers = []
    challenger_roads = []
    for cur_ver in [cache[-1]] + [cache[0]]:
        if matrix[cur_ver] != [0]*n:
            vers = [i for i in range(len(matrix[cur_ver])) if matrix[cur_ver][i] != 0]
            for ver in vers:
                if ver in cache:
                    pass
                else:
                    challenger_roads.append(min([matrix[cur_ver][i] for i in range(n) if (matrix[cur_ver][i] != 0 and not(i in cache))]))
                    challenger_vers.append(matrix[cur_ver].index(challenger_roads[-1]))
    i = challenger_roads.index(min(challenger_roads))        
    nearest_neighbour_roads.append(challenger_roads[i])
    cache.append(challenger_vers[i])

    count += 1
    if count > 100:
        # broken path
        nearest_neighbour_roads = [inf]
        break

# closing the loop
nearest_neighbour_roads.append(matrix[cache[-1]][cache[0]])
cache.append(cache[0])

print('Сlosest city inclusion method:', sum(nearest_neighbour_roads))

# Dynamic algorithm

inf = math.inf
dp = [[inf] * n for i in range(2**n)]
dp[0][0] = 0

for mask in range(2**n):
    for i in range(n):
        if dp[mask][i] == inf:
            continue
        for j in range(n):
            if not(mask & (1 << j)):
                dp[mask ^ (1 << j)][j] = min(dp[mask ^ (1 << j)][j], dp[mask][i] + matrix[i][j])

print('Dynamic algorithm:', dp[2**n - 1][0])

def findWay():    
    way = []
    i = 0
    mask = 2**n - 1
    way.append(0)
    while mask != 0:
        for j in range(n):
            if matrix[j][i] != 0 and (((mask >> j) & 1 == 1) or len(way) == n) and (dp[mask][i] == dp[mask ^ 2**i][j] + matrix[j][i]): 
                way.append(j)
                mask = mask ^ 2**i
                i = j
    return(way[::-1])
    
print(findWay())