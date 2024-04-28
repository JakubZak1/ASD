import numpy as np
from copy import deepcopy


class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


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
        if Node(vertex1) not in self.vertices:
            self.insertVertex(vertex1)
        if Node(vertex2) not in self.vertices:
            self.insertVertex(vertex2)
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        self.matrix[idx1][idx2] = edge
        self.matrix[idx2][idx1] = edge

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
        self.matrix[idx2][idx1] = self.val

    def getVertexIdx(self, vertex):
        return self.vertices.index(Node(vertex))

    def getVertex(self, vertex_idx):
        return self.vertices[vertex_idx]

    def neighbours(self, vertex_idx):
        return self.matrix[vertex_idx]

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


def is_isomorphic(g, p, m):
    x = m @ np.transpose(m @ g)
    return np.array_equal(x, p)


def ullman1(g, p, m=None, row=0, used_cols=None, recursion_count=0, isomorphism_count=0):
    recursion_count += 1

    if m is None:
        m = np.zeros((p.shape[0], g.shape[0]))
    if used_cols is None:
        used_cols = []

    if row == len(m):
        row -= 1
        if is_isomorphic(g, p, m):
            isomorphism_count += 1
        return isomorphism_count, recursion_count

    m_copy = deepcopy(m)
    for col in range(len(m[0])):
        if col not in used_cols:
            used_cols.append(col)
            m_copy[row, :] = 0
            m_copy[row, col] = 1
            isomorphism_count, recursion_count = ullman1(g, p, m_copy, row + 1, used_cols, recursion_count, isomorphism_count)
            used_cols.remove(col)

    return isomorphism_count, recursion_count


def degree(matrix, idx):
    count = 0
    for i in range(len(matrix[0])):
        if matrix[idx][i] == 1:
            count += 1
    return count


def m0(g, p):
    m = np.zeros((p.shape[0], g.shape[0]))
    for i in range(p.shape[0]):
        for j in range(g.shape[0]):
            if degree(p, i) <= degree(g, j):
                m[i][j] = 1
    return m


def ullman2(g, p, m0, m=None, row=0, used_cols=None, recursion_count=0, isomorphism_count=0):
    recursion_count += 1

    if m is None:
        m = np.zeros((p.shape[0], g.shape[0]))
    if used_cols is None:
        used_cols = []

    if row == len(m):
        row -= 1
        if is_isomorphic(g, p, m):
            isomorphism_count += 1
        return isomorphism_count, recursion_count

    m_copy = deepcopy(m)
    for col in range(len(m[0])):
        if col not in used_cols and m0[row][col] == 1:
            used_cols.append(col)
            m_copy[row, :] = 0
            m_copy[row, col] = 1
            isomorphism_count, recursion_count = ullman2(g, p, m0, m_copy, row + 1, used_cols, recursion_count, isomorphism_count)
            used_cols.remove(col)

    return isomorphism_count, recursion_count


def prune(g, p, m):
    changed = False

    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m[i][j] == 1:
                p_neighbors = [idx for idx, val in enumerate(p[i]) if val == 1]
                g_neighbors = [idx for idx, val in enumerate(g[j]) if val == 1]

                matching_neighbor_exists = any(m[x][y] == 1 for x in p_neighbors for y in g_neighbors)

                if not matching_neighbor_exists:
                    m[i][j] = 0
                    changed = True

    return changed


def ullman3(g, p, m0, m=None, row=0, used_cols=None, recursion_count=0, isomorphism_count=0):
    recursion_count += 1

    if m is None:
        m = np.zeros((p.shape[0], g.shape[0]))
    if used_cols is None:
        used_cols = []

    if row == len(m):
        row -= 1
        if is_isomorphic(g, p, m):
            isomorphism_count += 1
        return isomorphism_count, recursion_count

    m_copy = deepcopy(m)
    if row == len(m) - 1:
        prun = prune(g, p, m_copy)
    else:
        prun = False
    for col in range(len(m[0])):
        if prun is True and row != 0:
            break
        if col not in used_cols and m0[row][col] == 1:
            used_cols.append(col)
            m_copy[row, :] = 0
            m_copy[row, col] = 1
            isomorphism_count, recursion_count = ullman3(g, p, m0, m_copy, row + 1, used_cols, recursion_count, isomorphism_count)
            used_cols.remove(col)

    return isomorphism_count, recursion_count


if __name__ == '__main__':
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]
    g_graph = Macierz()
    for el in graph_G:
        v1 = Node(el[0])
        v2 = Node(el[1])
        g_graph.insertEdge(v1, v2)

    p_graph = Macierz()
    for el in graph_P:
        v1 = Node(el[0])
        v2 = Node(el[1])
        p_graph.insertEdge(v1, v2)

    g = np.array(g_graph.matrix)
    p = np.array(p_graph.matrix)
    m0 = m0(g, p)

    u1 = ullman1(g, p)
    u2 = ullman2(g, p, m0)
    u3 = ullman3(g, p, m0)
    print(u1)
    print(u2)
    print(u3)
