def print_matrix(matrix):
    """
    Prints the input matrix.
    Args: 
        matrix: 2D list
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()

def transpose(matrix):
    """
    Takes transpose of the input matrix.
    Args: 
        matrix: 2D list
    Return:
        result: 2D list
    """
    result = [[matrix[col][row] for col in range(len(matrix))] for row in range(len(matrix[0])) ]

    return result

def sum_of_matrices(matrix1, matrix2):
    """
    Sums the input matrices (matrix1 + matrix2). If dimension sizes are not match returns -1!
    Args: 
        matrix1: 2D list
        matrix2: 2D list
    Return:
        result: 2D list. If dimension sizes are not match returns -1!
        result = []
    """
    result = [[0 for i in range(len(matrix1))] for i in range(len(matrix1))]

    if len(matrix1)==len(matrix2) and len(matrix1[0])==len(matrix2[0]):
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                result[i][j] = matrix1[i][j]+matrix2[i][j]
        return result
    else:
        print('Error dimension sizes of the matrixes are not the same')
        return -1

    

def difference_of_matrices(matrix1, matrix2):
    """
    Takes diffirence of the input matrices (matrix1 - matrix2). If dimension sizes are not match returns -1!
    Args: 
        matrix1: 2D list
        matrix2: 2D list
    Return:
        result: 2D list. If dimension sizes are not match returns -1!
    """
    result = [[0 for i in range(len(matrix1))] for i in range(len(matrix1))]

    if len(matrix1)==len(matrix2) and len(matrix1[0])==len(matrix2[0]):
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                result[i][j] = matrix1[i][j]-matrix2[i][j]
        return result
    else:
        print('Error dimension sizes of the matrixes are not the same')
        return -1
    

    return result

def multiply_matrices(matrix1, matrix2):
    """
    Multiplies the matrices (matrix1 * matrix2) (cross product). If dimension sizes are not match returns -1!
    Args: 
        matrix1: 2D list
        matrix2: 2D list
    Return:
        result: 2D list. If dimension sizes are not match returns -1!
    """
    if len(matrix1[0])==len(matrix2):
        result = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
        Tmatrix2 = transpose(matrix2)
        for k in range(len(Tmatrix2)):
            for i in range(len(matrix1)):
                sumrow = 0
                for j in range(len(matrix1[0])):
                    sumrow+=(matrix1[i][j]*Tmatrix2[k][j])
                result[i][k]=sumrow

        return result
    else:
        print('Error dimension sizes of the matrixes are not the same')
        return -1

def determinant(matrix):
    """
    Calculates the determinant of input matrix.
    # Hint: Think recursive.
    # Another hint: Base case is 2x2 matrix.
    Args: 
        matrix: 2D list
    Return:
        result: Integer
    """
    result = 0
    if len(matrix)!=len(matrix[0]):
        return -1
    else:
        if len(matrix)==2:
            mult1 = matrix[0][0]*matrix[1][1]
            mult2 = matrix[1][0]*matrix[0][1]
            return mult1-mult2

        else:
            for col in range(len(matrix[0])):
                matrix_copy = [row[:] for row in matrix]
                matrix_cropped = matrix_copy[1:]
                for i in range(len(matrix_cropped)):
                    matrix_cropped[i].pop(col)
                if col%2==0:sign=1
                elif col%2==1:sign=-1
                result+=(sign)*matrix[0][col]*determinant(matrix_cropped)

    return result



def read_matrix():
    """
    Reads square matrix from user.
    First take an integer from user.
    Then reads inputs from user and cast it as integer.
    Returns the read matrix
    Args: 
    Return:
        result: 2D Matrix
    """
    first_size = int(input())
    result = []
    for row in range(first_size):
        row = input()
        result.append([int(i) for i in row.split()])

    return result



# do not change below:
if __name__ == "__main__":
    A = read_matrix()
    B = read_matrix()

        
    print("Matrix A:")
    print_matrix(A)

    print("Matrix B:")
    print_matrix(B)

    transpose_A = transpose(A)
    print("Transpose of Matrix A:")
    print_matrix(transpose_A)

    transpose_B = transpose(B)
    print("Transpose of Matrix B:")
    print_matrix(transpose_B)

    print("A + B:")
    result = sum_of_matrices(A, B)
    if result != -1:
        print_matrix(result)

    print("A - B:")
    result = difference_of_matrices(A, B)
    if result != -1:
        print_matrix(result)
    
    print("A * B:")
    result = multiply_matrices(A, B)
    if result != -1:
        print_matrix(result)

    print("B * A:")
    result = multiply_matrices(B, A)
    if result != -1:
        print_matrix(result)

    print(f"Determinant of Matrix A: {determinant(A)}")
    print(f"Determinant of Matrix B: {determinant(B)}")
