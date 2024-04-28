import polska


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


class Lista:
    def __init__(self):
        self.dict = {}
        self.vertices = []

    def isEmpty(self):
        return self.dict == []

    def insertVertex(self, vertex):
        self.dict[Node(vertex)] = []
        self.vertices.append(Node(vertex))

    def insertEdge(self, vertex1, vertex2):
        if ((vertex1, vertex2) not in self.edges()) and ((vertex2, vertex1) not in self.edges()):
            self.dict[Node(vertex1)].append(Node(vertex2))
            self.dict[Node(vertex2)].append(Node(vertex1))

    def deleteVertex(self, vertex):
        self.dict.pop(Node(vertex))
        for item, value in self.dict.items():
            if Node(vertex) in value:
                value.remove(Node(vertex))
        self.vertices.remove(Node(vertex))

    def deleteEdge(self, vertex1, vertex2):
        self.dict[Node(vertex1)].remove(Node(vertex2))
        self.dict[Node(vertex2)].remove(Node(vertex1))

    def getVertexIdx(self, vertex):
        return self.vertices.index(Node(vertex))

    def getVertex(self, vertex_idx):
        return self.vertices[vertex_idx]

    def neighbours(self, vertex_idx):
        vertex = self.getVertex(vertex_idx)
        return self.dict[vertex]

    def order(self):
        return len(self.dict)

    def size(self):
        counter = 0
        for key, value in self.dict.items():
            counter += len(value)
        return counter / 2

    def edges(self):
        lst = []
        for key, value in self.dict.items():
            for neighbour in value:
                lst.append((key.key, neighbour.key))
        return lst


def main():
    vertices = [tup[2] for tup in polska.polska]
    edges = polska.graf

    macierz = Macierz()
    lista = Lista()
    for node in vertices:
        macierz.insertVertex(node)
        lista.insertVertex(node)
    for edge in edges:
        macierz.insertEdge(edge[0], edge[1])
        lista.insertEdge(edge[0], edge[1])
    macierz.deleteVertex('K')
    macierz.deleteEdge('E', 'W')
    lista.deleteVertex('K')
    lista.deleteEdge('E', 'W')

    polska.draw_map(macierz.edges())
    polska.draw_map(lista.edges())


if __name__ == '__main__':
    main()
