import numpy as np

def get_matrix_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    print(f"Enter the matrix elements row by row, separated by spaces:")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Error: Column count does not match!")
            return None
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def add_matrices():
    print("Matrix Addition")
    print("Enter first matrix:")
    A = get_matrix_input()
    print("Enter second matrix:")
    B = get_matrix_input()
    
    if A.shape != B.shape:
        print("Error: must have the same dimensions!")
        return
    
    result = A + B
    print("Result of matrix addition:")
    display_matrix(result)

def subtract_matrices():
    print("Matrix Subtraction")
    print("Enter first matrix:")
    A = get_matrix_input()
    print("Enter second matrix:")
    B = get_matrix_input()

    if A.shape != B.shape:
        print("Error: Matrices must have the same dimensions!")
        return

    result = A - B
    print("Result of matrix subtraction:")
    display_matrix(result)

def multiply_matrices():
    print("Matrix Multiplication")
    print("Enter first matrix:")
    A = get_matrix_input()
    print("Enter second matrix:")
    B = get_matrix_input()

    if A.shape[1] != B.shape[0]:
        print("Error: Number of columns of first matrix must equal number of rows of second matrix!")
        return

    result = A.dot(B)
    print("Result of matrix multiplication:")
    display_matrix(result)

def transpose_matrix():
    print("Matrix Transpose")
    print("Enter matrix:")
    A = get_matrix_input()
    result = A.T
    print("Transpose of matrix:")
    display_matrix(result)

def scalar_multiplication():
    print("Scalar Multiplication")
    print("Enter matrix:")
    A = get_matrix_input()
    scalar = int(input("Enter scalar value: "))
    result = A * scalar
    print(f"Result of multiplying matrix by {scalar}:")
    display_matrix(result)

def calculate_determinant():
    print("Matrix Determinant (for square matrices only)")
    A = get_matrix_input()
    if A.shape[0] != A.shape[1]:
        print("Error: Determinant is only for square matrices!")
        return

    result = np.linalg.det(A)
    print(f"Determinant of matrix: {result}")

def calculate_inverse():
    print("Matrix Inverse (for square matrices only)")
    A = get_matrix_input()
    if A.shape[0] != A.shape[1]:
        print("Error: Inverse is only for square matrices!")
        return

    det = np.linalg.det(A)
    if det == 0:
        print("Error: Matrix is non-invertible!")
        return

    result = np.linalg.inv(A)
    print("Inverse of matrix:")
    display_matrix(result)

def calculate_trace():
    print("Matrix Trace (for square matrices only)")
    A = get_matrix_input()
    if A.shape[0] != A.shape[1]:
        print("Error: Trace is only for square matrices!")
        return

    result = np.trace(A)
    print(f"Trace of matrix: {result}")

def menu():
    while True:
        print("\nMatrix Operations Program")
        print("===========================")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Transpose a Matrix")
        print("5. Scalar Multiplication")
        print("6. Calculate Determinant")
        print("7. Calculate Inverse")
        print("8. Calculate Trace")
        print("9. Exit")
        choice = input("Please select an operation (1-9): ")

        if choice == '1':
            add_matrices()
        elif choice == '2':
            subtract_matrices()
        elif choice == '3':
            multiply_matrices()
        elif choice == '4':
            transpose_matrix()
        elif choice == '5':
            scalar_multiplication()
        elif choice == '6':
            calculate_determinant()
        elif choice == '7':
            calculate_inverse()
        elif choice == '8':
            calculate_trace()
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
