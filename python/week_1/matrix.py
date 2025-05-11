class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [
            [int(char) for char in string.split()]
        for string in matrix_string.splitlines()
        ]

    def row(self, index):
        return self.matrix[index - 1]


    def column(self, index):
        column = []
        for row in self.matrix:
            column.append(row[index -1])
        return column


def print_result():
    # matrix_string = "9 8 7\n5 3 2\n6 6 7"
    # m = Matrix(matrix_string)
    m = Matrix("1")
    print(m.matrix)
    print(m.row(0))
    print(m.column(0))

if __name__ == '__main__':
    print_result()