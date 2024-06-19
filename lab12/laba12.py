#Task 1
def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    self.data = [[0] * columns for _ in range(rows)]
#Task 2
def add_element(self, row, column, value):
    if 0 <= row < self.rows and 0 <= column < self.columns:
        self.data[row][column] = value
    else:
        raise IndexError("Index out of range")

#Task 3
def sum_of_rows(self):
    return [sum(row) for row in self.data]

#Task 4
def transpose(self):
    transposed = Matrix(self.columns, self.rows)
    for i in range(self.rows):
        for j in range(self.columns):
            transposed.data[j][i] = self.data[i][j]
    return transposed

#Task 5
def multiply_by(self, other):
    if self.columns != other.rows:
        raise ValueError("Number of columns of the first matrix must be equal to the number of rows of the second matrix")
    
    result = Matrix(self.rows, other.columns)
    for i in range(self.rows):
        for j in range(other.columns):
            for k in range(self.columns):
                result.data[i][j] += self.data[i][k] * other.data[k][j]
    return result

#Task 6
def is_symmetric(self):
    if self.rows != self.columns:
        return False
    
    for i in range(self.rows):
        for j in range(i + 1, self.columns):
            if self.data[i][j] != self.data[j][i]:
                return False
    return True

#Task 7
def rotate_right(self):
    rotated = Matrix(self.columns, self.rows)
    for i in range(self.rows):
        for j in range(self.columns):
            rotated.data[j][self.rows - 1 - i] = self.data[i][j]
    return rotated

#Task 8
def flatten(self):
    flattened = []
    for row in self.data:
        flattened.extend(row)
    return flattened

#Task 9
@staticmethod
def from_list(list_of_lists):
    rows = len(list_of_lists)
    columns = len(list_of_lists[0])
    matrix = Matrix(rows, columns)
    for i in range(rows):
        for j in range(columns):
            matrix.data[i][j] = list_of_lists[i][j]
    return matrix

#Task 10
def diagonal(self):
    if self.rows != self.columns:
        raise ValueError("Matrix must be square to extract diagonal")
    
    return [self.data[i][i] for i in range(self.rows)]
