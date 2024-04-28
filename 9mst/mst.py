import graf_mst


class Node:
    def __init__(self, key, color=None):
        self.key = key
        self.color = color

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return f'{self.key}'

    def __repr__(self):
        return f'{self.key}'


class Lista:
    def __init__(self):
        self.dict = {}
        self.vertices = []
        self.costs = []

    def isEmpty(self):
        return self.dict == {}

    def insertVertex(self, vertex):
        self.dict[Node(vertex)] = []
        self.vertices.append(Node(vertex))

    def insertEdge(self, vertex1, vertex2, cost=1):
        if ((vertex1, vertex2) not in self.edges()) and ((vertex2, vertex1) not in self.edges()):
            self.dict[Node(vertex1)].append(Node(vertex2))
            self.dict[Node(vertex2)].append(Node(vertex1))
        self.costs.append((Node(vertex1), Node(vertex2), cost))

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
        return self.vertices.index(vertex)

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

    def neighbours_costs(self, vertex_idx):
        lst = []
        vertex = self.getVertex(vertex_idx)
        for elem in self.costs:
            if elem[0] == vertex:
                lst.append((self.getVertexIdx(elem[1]), elem[2]))
        return lst

    def mst(self):
        result = Lista()

        for vertex in self.dict:
            result.insertVertex(vertex)

        intree = {node: 0 for node in self.dict.keys()}
        distance = {node: float('inf') for node in self.dict.keys()}
        parent = {node: -1 for node in self.dict.keys()}

        v = self.getVertex(0)
        costs = 0

        while intree[v] == 0:
            v_idx = self.getVertexIdx(v)
            intree[v] = 1

            for idx, cost in self.neighbours_costs(v_idx):
                if cost < distance[v] and intree[self.getVertex(idx)] == 0:
                    distance[v] = cost
                    parent[v] = self.getVertex(idx)

            min_cost = float('inf')
            next = None

            for vertex in self.dict.keys():
                if intree[vertex] == 0:
                    if min_cost >= distance[vertex]:
                        min_cost = distance[vertex]
                        next = vertex

            if next is not None:
                result.insertEdge(v, parent[v], distance[v])
                result.insertEdge(parent[v], v, distance[v])
                costs += distance[v]
                v = next

        return result, costs


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours_costs(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")


if __name__ == '__main__':
    graf = graf_mst.graf
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    gl = Lista()
    for elem in nodes:
        gl.insertVertex(elem)
    for elem in graf:
        gl.insertEdge(elem[0], elem[1], elem[2])
        gl.insertEdge(elem[1], elem[0], elem[2])

    mst, cost = gl.mst()
    printGraph(mst)
    