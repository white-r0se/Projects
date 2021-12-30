import random

class graph:
    def __init__(self, vertices, edges) -> None:        
        print(f'Граф: {vertices} вершин, {edges} ребер')
        self.matrix = [[0 for i in range(edges)] for j in range(vertices)]
        print(f'Введите через пробел номера вершин откуда и куда идет дорога')
        
        # Создание матрицы инцидентности и определение весов ребер
        roads = []
        self.weight = {}
        for i in range(edges):
            a1, a2 = map(int, input(f'{i+1} дорога:').split())
            if a1 == a2:
                self.matrix[a1-1][i] = 2
            else:
                self.matrix[a1-1][i] = 1
                self.matrix[a2-1][i] = -1
            roads.append((a1, a2))
            if (a2, a1) in roads:
                self.weight[i] = self.weight[roads.index((a2, a1))]
            else:
                self.weight[i] = random.randint(1, 30)
                
        
    def search_rec(self, curvertice, find, curtime, cache) -> None:
        '''Рекурсивный поиск вершины'''
        if curvertice == find:
            self.roads.append(curtime)
        if 1 in self.matrix[curvertice]:
            for road in range(len(self.matrix[curvertice])):
                if self.matrix[curvertice][road] == 1:
                    for vertice in range(len(self.matrix)):
                        if self.matrix[vertice][road] == -1 and not(vertice in cache):
                            self.search_rec(vertice, find, curtime + self.weight[road], cache + [vertice])

    def search(self, a, b):
        '''
        Поиск минимального времени для того, чтобы добраться из a в b
        Возвращает int - кол-во минут
        '''
        cache = []
        self.roads = []
        self.search_rec(a, b, 0, cache)
        return min(self.roads)

    def input_search(self):
        a, b = map(int, input('Введите через пробел номера вершин откуда и куда вам нужно попасть:').split())
        print(f'Это займет {self.search(a-1, b-1)} минут')


g = graph(5, 8)
g.input_search()
# 1 2
# 2 3
# 2 5
# 3 5
# 3 4
# 5 4
# 4 5
# 5 1