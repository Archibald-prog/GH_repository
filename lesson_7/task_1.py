class Matrix:
    def __init__(self, matrix_structure):
        self.matrix = matrix_structure

    def __str__(self):
        return '\n'.join([' '.join([map(lambda x: str(x), self.matrix)]) for line in self.matrix])

    def __add__(self, other):
        result = ''
        if len(self.matrix) == len(other.matrix):
            for line_1, line_2 in zip(self.matrix, other.matrix):
                if len(line_1) != len(line_2):
                    return 'Number of elements must be equal'

                sum_line = [x + y for x, y in zip(line_1, line_2)]
                result += ' '.join(map(lambda x: str(x), sum_line)) + '\n'

        else:
            return 'Number of elements must be equal'
        return result


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])

print(matrix_1 + matrix_2)
