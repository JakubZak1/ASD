import numpy as np
from collections import deque
# class Lista:
#     def __init__(self):
#         self.dict = {}
#         self.vertices = []
#         self.costs = []
#
#     def isEmpty(self):
#         return self.dict == {}
#
#     def insertVertex(self, vertex):
#         self.dict[Node(vertex)] = []
#         self.vertices.append(Node(vertex))
#
#     def insertEdge(self, vertex1, vertex2, cost):
#         if (vertex1, vertex2) not in self.edges():
#             self.dict[Node(vertex1)].append(Node(vertex2))
#             # self.dict[Node(vertex2)].append(Node(vertex1))
#         self.costs.append((Node(vertex1), Node(vertex2), cost))
#
#     def deleteVertex(self, vertex):
#         self.dict.pop(Node(vertex))
#         for item, value in self.dict.items():
#             if Node(vertex) in value:
#                 value.remove(Node(vertex))
#         self.vertices.remove(Node(vertex))
#
#     def deleteEdge(self, vertex1, vertex2):
#         self.dict[Node(vertex1)].remove(Node(vertex2))
#         # self.dict[Node(vertex2)].remove(Node(vertex1))
#
#     def getVertexIdx(self, vertex):
#         return self.vertices.index(vertex)
#
#     def getVertex(self, vertex_idx):
#         return self.vertices[vertex_idx]
#
#     def neighbours(self, vertex_idx):
#         vertex = self.getVertex(vertex_idx)
#         return self.dict[vertex]
#
#     def order(self):
#         return len(self.dict)
#
#     def size(self):
#         counter = 0
#         for key, value in self.dict.items():
#             counter += len(value)
#         return counter / 2
#
#     def edges(self):
#         lst = []
#         for key, value in self.dict.items():
#             for neighbour in value:
#                 lst.append((key.key, neighbour.key))
#         return lst
#
#     def neighbours_costs(self, vertex_idx):
#         lst = []
#         vertex = self.getVertex(vertex_idx)
#         for elem in self.costs:
#             if elem[0] == vertex:
#                 lst.append((self.getVertexIdx(elem[1]), elem[2]))
#         return lst
#
#     # def neighbours_costs(self, vertex_idx):
#     #     lst = []
#     #     vertex = self.getVertex(vertex_idx)
#     #     for elem in self.costs:
#     #         if elem[0] == vertex:
#     #             lst.append((elem[1], elem[2]))
#     #     return lst
#
#     def getEdge(self, v1, v2):
#         for edge in self.costs:
#             if edge[0] == v1 and edge[1] == v2:
#                 return edge[2]

class Edge:
    def __init__(self, capacity, isResidual=False):
        self.capacity = capacity
        self.isResidual = isResidual
        self.flow = 0
        self.residual = capacity

    def __repr__(self):
        rep = str(self.capacity) + ' ' + str(self.flow) + ' ' + str(self.residual) + ' ' + str(self.isResidual)
        return rep


class Node:
    def __init__(self, key, color=None):
        self.key = key
        self.color = color

    def __eq__(self, other):
        if type(other) != Node:
            return self.key == other
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return f'{self.key}'

    def __repr__(self):
        return f'{self.key}'




class Macierz:
    def __init__(self, val=0):
        self.matrix = []
        self.vertices = []
        self.val = val

    def isEmpty(self):
        return self.matrix == []

    def insertVertex(self, vertex):
        if self.isEmpty():
            self.matrix.append([self.val])
        else:
            for line in self.matrix:
                line.append(self.val)
            self.matrix.append([self.val for _ in range(self.order() + 1)])
        self.vertices.append(Node(vertex))

    def insertEdge(self, vertex1, vertex2, edge=1):
        if vertex1 not in self.vertices:
            self.insertVertex(vertex1)
        if vertex2 not in self.vertices:
            self.insertVertex(vertex2)
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        self.matrix[idx1][idx2] = edge
        # self.matrix[idx2][idx1] = edge

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)
        self.matrix.pop(idx)
        self.vertices.remove(Node(vertex))
        for line in self.matrix:
            line.pop(idx)

    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        self.matrix[idx1][idx2] = self.val
        # self.matrix[idx2][idx1] = self.val

    def getVertexIdx(self, vertex):
        return self.vertices.index(Node(vertex))

    def getVertex(self, vertex_idx):
        return self.vertices[vertex_idx]

    def neighbours(self, vertex_idx):
        result_list = []
        for i in range(len(self.matrix[vertex_idx])):
            if not self.matrix[vertex_idx][i] == 0:
                result_list.append((i, self.matrix[vertex_idx][i]))
        return result_list

    def order(self):
        return len(self.matrix)

    def size(self):
        counter = 0
        for i in range(self.order()):
            for j in range(self.order()):
                if self.matrix[i][j] != self.val:
                    counter += 1
        return counter / 2

    def edges(self):
        edges = []
        for i in range(self.order()):
            for j in range(self.order()):
                if self.matrix[i][j] != self.val and self.matrix[j][i] != self.val:
                    edges.append((self.getVertex(i).key, self.getVertex(j).key))
        return edges

    # def get_edge(self, vertex1, vertex2):
    #     idx1 = self.getVertexIdx(vertex1)
    #     idx2 = self.getVertexIdx(vertex2)
    #     return Edge(self.matrix[idx1][idx2])

    def bfs(self, s):
        visited = {s: None}
        unvisited = [s]
        while unvisited:
            v = unvisited.pop()
            for el, w in self.neighbours(v):
                if el not in visited.keys() and w.residual > 0:
                    unvisited.insert(0, el)
                    visited[el] = v
        return visited

    # def bfs(self, s):
    #     visited = [0] * self.order()
    #     parent = [-1] * self.order()
    #     queue = [s]
    #     visited[s] = 1
    #
    #     while queue:
    #         elem = queue.pop(0)
    #         neighbours = self.neighbours(elem)
    #
    #         for neighbour, edge in neighbours:
    #             if visited[neighbour] == 0 and edge.residual > 0:
    #                 queue.append(neighbour)
    #                 visited[neighbour] = 1
    #                 parent[neighbour] = elem
    #
    #     return parent

    def analiz(self, s, k, parent_list):
        min_capacity = float('inf')
        vertex = k
        try:
            c = parent_list[vertex]
        except KeyError:
            return 0
        while vertex != s:
            parent = parent_list[vertex]
            edge = self.matrix[parent][vertex]
            if edge.residual < min_capacity:
                min_capa = edge.residual
            v = parent
        return min_capacity

    # def lowest_capacity(self, parent, start_vertex, end_vertex):
    #     current_vertex = end_vertex
    #     min_capacity = float('inf')
    #
    #     if parent[current_vertex] is None:
    #         return 0
    #     try:
    #         c = parent[current_vertex]
    #     except KeyError:
    #         return None
    #
    #     while current_vertex != start_vertex:
    #         parent_vertex = parent[current_vertex]
    #         edge = self.get_edge(parent_vertex, current_vertex)
    #         residual_capacity = edge.residual
    #
    #         if residual_capacity < min_capacity:
    #             min_capacity = residual_capacity
    #
    #         current_vertex = parent_vertex
    #
    #     print(min_capacity)
    #     return min_capacity

    def aug_path(self, s, k, parent_list, min_capa):
        v = k
        try:
            c = parent_list[v]
        except KeyError:
            return None
        while v != s:
            parent = parent_list[v]
            edge = self.matrix[parent][v]
            virtual = self.matrix[v][parent]
            edge.flow += min_capa
            edge.residual -= min_capa
            virtual.residual += min_capa
            v = parent

    # def augmentation(self, start_vertex, end_vertex, parent, min_capacity):
    #     current_vertex = end_vertex
    #
    #     while current_vertex != start_vertex:
    #         parent_vertex = parent[current_vertex]
    #
    #         # Aktualizacja przepływu dla krawędzi "rzeczywistej"
    #         edge_real = self.get_edge(parent_vertex, current_vertex)
    #         edge_real.flow += min_capacity
    #         edge_real.residual -= min_capacity
    #
    #         # Aktualizacja przepływu resztowego dla krawędzi "resztowej"
    #         edge_residual = self.get_edge(current_vertex, parent_vertex)
    #         edge_residual.residual += min_capacity
    #
    #         current_vertex = parent_vertex

    def main_fun(self, s, k):
        sum = 0
        parent_list = self.bfs(s)
        min_c = self.analiz(s, k, parent_list)
        while min_c > 0:
            self.aug_path(s, k, parent_list, min_c)
            parent_list = self.bfs(s)
            min_c = self.analiz(s, k, parent_list)
        for i in range(len(self.matrix)):
            if self.matrix[i][k] != 0:
                sum += self.matrix[i][k].flow
        return sum

    # def ford_fulkerson(self, start_vertex, end_vertex):
    #     max_flow = 0
    #
    #     # Tworzenie listy parent
    #     parent = self.bfs(start_vertex)
    #
    #     # Dopóki istnieje ścieżka od wierzchołka początkowego do końcowego
    #     while parent[end_vertex] is not None:
    #         # Obliczanie minimalnego przepływu dla ścieżki
    #         min_capacity = self.lowest_capacity(parent, start_vertex, end_vertex)
    #
    #         # Augmentacja ścieżki
    #         self.augmentation(start_vertex, end_vertex, parent, min_capacity)
    #
    #         # Aktualizacja listy parent
    #         parent = self.bfs(start_vertex)
    #
    #         # Dodawanie minimalnego przepływu do maksymalnego przepływu
    #         max_flow += min_capacity
    #
    #     return max_flow

def printgraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i).key
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j).key, w, end=";")
        print()
    print("-------------------")

graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9),
          ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
          ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
          ('d', 'c', 4)]
g = [graf_0, graf_1, graf_2, graf_3]
for i in range(4):
    graf = g[i]
    test = Macierz()
    for el in graf:
        v1 = Node(el[0])
        v2 = Node(el[1])
        edge = Edge(el[2])
        res_edge = Edge(0, True)
        test.insertEdge(v1, v2, edge)
        if test.matrix[test.getVertexIdx(v2)][test.getVertexIdx(v1)] == 0:
            test.insertEdge(v2, v1, res_edge)
    start_vertex = Node('s')  # Create a Node object for the start vertex
    end_vertex = Node('t')  # Create a Node object for the end vertex
    start_vertex_idx = test.getVertexIdx(start_vertex)
    end_vertex_idx = test.getVertexIdx(end_vertex)
    print(test.main_fun(start_vertex_idx, end_vertex_idx))
    printgraph(test)