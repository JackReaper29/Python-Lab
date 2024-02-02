def transpose(matrix):
    # Calculate the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with swapped rows and columns
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return transposed_matrix

def multiply_matrices(matrix1, matrix2):
    # Check if matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    # Initialize the result matrix with zeros
    result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

# Example matrices
matrix_a = [[1, 2, 3],
            [4, 5, 6]]

matrix_b = [[7, 8],
            [9, 10],
            [11, 12]]

# Transpose matrix A
transposed_a = transpose(matrix_a)
print("Transposed Matrix A:")
for row in transposed_a:
    print(row)

# Multiply matrices A and B
result_ab = multiply_matrices(matrix_a, matrix_b)
print("\nResult of Matrix Multiplication (A * B):")
for row in result_ab:
    print(row)
