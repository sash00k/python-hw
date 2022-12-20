def matrix_mul(a,b):
    if len(a[0]) != len(b):
        raise ValueError('The sizes of the matrices do not match')

    zip_b = list(zip(*b))
    result = [[sum(elem_a*elem_b for elem_a, elem_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]
    return result

def matrix_pow(matrix: list[list[int]], n: int) -> list[list[int]]:
    if len(matrix) != len(matrix[0]):
        raise ValueError('Powered matrix is not square')

    result = matrix.copy()
    for i in range(n-1):
        result = matrix_mul(result, matrix)

    return result

if __name__ == '__main__':
    mat = [[1, 2], [3, 4]]
    print(matrix_pow(mat, 3))