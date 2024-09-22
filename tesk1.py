import numpy as np

def get_matrix():
    # Initializing rows and columns
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix = [] 
    for row in range(rows):
        a = list(map(int, input().split()))
        if len(a) != columns:
            print("The column count does not match")
            return None
        matrix.append(a)
    return np.array(matrix)

def print_matrix(matrix):
    # Printing the matrix
    for row in matrix:
        print(" ".join(map(str, row)))

# Add matrix
def Add_matrix():
    print("Matrix Addition Operation")
    print("Enter Matrix A")
    A = get_matrix()
    print("Enter Matrix B")
    B = get_matrix()

    if A.shape != B.shape:
        print("Matrices must have the same dimensions")
        return

    res = A + B
    print("Result of the Matrix Addition is:")
    print_matrix(res)

# Subtract matrix
def sub_matrix():
    print("Matrix Subtraction Operation")
    print("Enter Matrix A")
    A = get_matrix()
    print("Enter Matrix B")
    B = get_matrix()

    if A.shape != B.shape:
        print("Matrices must have the same dimensions")
        return
    
    res = A - B
    print("Result of the Matrix Subtraction is:")
    print_matrix(res)

# Matrix multiplication
def mul_matrix():
    print("Matrix Multiplication Operation")
    print("Enter Matrix A")
    A = get_matrix()
    print("Enter Matrix B")
    B = get_matrix()

    if A.shape[1] != B.shape[0]:
        print("The column count of Matrix A should match the row count of Matrix B")
        return

    res = A.dot(B)
    print("Result of the Matrix Multiplication is:")
    print_matrix(res)

# Transpose matrix
def Transpose_Matrix():
    print("Matrix Transpose Operation")
    print("Enter Matrix A")
    A = get_matrix()

    res = A.transpose()
    print("The Transpose of Matrix A is:")
    print_matrix(res)

# Scalar multiplication
def Scalar_Matrix():
    print("Scalar Multiplication Operation")
    print("Enter Matrix A")
    A = get_matrix()
    scalar = int(input("Enter the scalar number: "))

    res = A * scalar
    print(f"The scalar multiplication of Matrix A with {scalar} is:")
    print_matrix(res)

# Calculate determinant
def calc_determinant():
    print("Determinant Calculation Operation")
    print("Enter a Square Matrix")
    A = get_matrix()

    if A.shape[0] != A.shape[1]:
        print("Error: Matrix must be square")
        return

    result = np.linalg.det(A)
    print(f"Determinant of the matrix is: {result}")

# Calculate inverse
def calc_inverse():
    print("Matrix Inverse Operation")
    print("Enter Matrix A")
    A = get_matrix()

    if A.shape[0] != A.shape[1]:
        print("Error: Matrix must be square")
        return

    det = np.linalg.det(A)
    if det == 0:
        print("The matrix is non-invertible")
        return

    res = np.linalg.inv(A)
    print("The inverse of Matrix A is:")
    print_matrix(res)

# Menu for matrix operations
def menu():
    while True:
        print("\nMatrix Operation Program")
        print("----------------------------")
        print("1. Add Matrix")
        print("2. Subtract Matrix")
        print("3. Matrix Multiplication")
        print("4. Matrix Transpose")
        print("5. Calculate Determinant")
        print("6. Calculate Inverse")
        print("7. Exit")

        choice = int(input("Please select an operation (1-7): "))

        if choice == 1:
            Add_matrix()
        elif choice == 2:
            sub_matrix()
        elif choice == 3:
            mul_matrix()
        elif choice == 4:
            Transpose_Matrix()
        elif choice == 5:
            calc_determinant()
        elif choice == 6:
            calc_inverse()
        elif choice == 7:
            print("Exiting the program")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
