import numpy as np

def gauss_jordan_inverse(matrix):
    """Calcula la inversa de una matriz usando Gauss-Jordan."""
    n = len(matrix)
    # Crear una matriz aumentada con la identidad a la derecha
    augmented = np.hstack((matrix, np.eye(n)))
    
    # Eliminación de Gauss-Jordan
    for i in range(n):
        # Escalar la fila para que el pivote sea 1
        pivot = augmented[i, i]
        if pivot == 0:
            raise ValueError("La matriz no es invertible.")
        augmented[i] = augmented[i] / pivot
        
        # Hacer ceros en las demás filas de la columna del pivote
        for j in range(n):
            if i != j:
                factor = augmented[j, i]
                augmented[j] -= factor * augmented[i]

    # La parte derecha de la matriz extendida es la inversa
    return augmented[:, n:]

def check_identity(matrix, inverse):
    """Verifica si matrix * inverse = identidad."""
    product = np.dot(matrix, inverse)
    identity = np.eye(len(matrix))
    return np.allclose(product, identity)

# Matrices proporcionadas

A = np.array([[3, 2, 2],
              [3, 1, -3],
              [1, 0, -2]], dtype=float)

B = np.array([[1, 2, 0, 4],
              [2, 0, -1, -2],
              [1, 1, -1, 0],
              [0, 4, 1, 0]], dtype=float)

# Calcular y verificar inversa para A
try:
    A_inv = gauss_jordan_inverse(A)
    print("Inversa de A:\n", A_inv)
    if check_identity(A, A_inv):
        print("La multiplicación A * A_inv da la identidad.")
    else:
        print("La multiplicación A * A_inv no da la identidad.")
except ValueError as e:
    print(f"Error para A: {e}")

# Calcular y verificar inversa para B
try:
    B_inv = gauss_jordan_inverse(B)
    print("\nInversa de B:\n", B_inv)
    if check_identity(B, B_inv):
        print("La multiplicación B * B_inv da la identidad.")
    else:
        print("La multiplicación B * B_inv no da la identidad.")
except ValueError as e:
    print(f"Error para B: {e}")
