class Matrix:
    def __init__(self, matrix, val=0):
        if isinstance(matrix, tuple):
            rows, cols = matrix
            self.matrix = [[val for _ in range(cols)] for _ in range(rows)]
        else:
            self.matrix = matrix

    def __add__(self, other):
        if self.size() == other.size():
            rows, cols = self.size()
            new_matrix = Matrix(matrix=(rows, cols))
            for i in range(rows):
                for j in range(cols):
                    new_matrix[i][j] = self.matrix[i][j] + other[i][j]
            return new_matrix
        else:
            return None

    def __mul__(self, other):
        if self.size()[1] == other.size()[0]:
            self_rows, _ = self.size()
            other_rows, other_cols = other.size()
            new_matrix = Matrix(matrix=(self_rows, other_cols))
            for i in range(self_rows):
                for j in range(other_cols):
                    for k in range(other_rows):
                        new_matrix[i][j] += self.matrix[i][k] * other[k][j]
            return new_matrix
        else:
            return None

    def __getitem__(self, item):
        return self.matrix[item]

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += "".join(str(row)) + "\n"
        return matrix_str

    def size(self):
        return len(self.matrix), len(self.matrix[0])


def transpose(matrix):
    rows, cols = matrix.size()
    new_matrix = Matrix([[0 for _ in range(rows)] for _ in range(cols)])
    for i in range(cols):
        for j in range(rows):
            new_matrix[i][j] = matrix[j][i]
    return new_matrix


def main():
    m1 = Matrix(
        [[1, 0, 2],
         [-1, 3, 1]])

    m2 = Matrix(matrix=(2, 3), val=1)

    m3 = Matrix(
        [[3, 1],
         [2, 1],
         [1, 0]])
    mt = transpose(m1)

    print(m1)
    print(mt)
    print(m1 + m2)
    print(m1 * m3)


if __name__ == '__main__':
    main()
