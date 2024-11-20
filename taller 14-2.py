import numpy as np

def operaciones_matrices():
    # Solicitar dimensiones de las matrices
    filas_a = int(input("Ingrese el número de filas de la matriz A: "))
    columnas_a = int(input("Ingrese el número de columnas de la matriz A: "))
    
    filas_b = int(input("Ingrese el número de filas de la matriz B: "))
    columnas_b = int(input("Ingrese el número de columnas de la matriz B: "))
    
    # Verificar si las dimensiones son compatibles para la multiplicación de matrices
    if columnas_a != filas_b:
        print("Las matrices no pueden multiplicarse (columnas de A deben ser iguales a filas de B).")
        return
    
    # Crear matrices A y B
    print("Ingrese los elementos de la matriz A:")
    A = np.array([[float(input(f"Elemento A[{i+1},{j+1}]: ")) for j in range(columnas_a)] for i in range(filas_a)])
    
    print("Ingrese los elementos de la matriz B:")
    B = np.array([[float(input(f"Elemento B[{i+1},{j+1}]: ")) for j in range(columnas_b)] for i in range(filas_b)])
    
    # Operaciones solicitadas
    print("\nOperaciones:")
    
    # 2A
    print("2A:")
    print(2 * A)
    
    # 3B
    print("3B:")
    print(3 * B)
    
    # A + B
    if A.shape == B.shape:
        print("A + B:")
        print(A + B)
    else:
        print("Las matrices A y B no tienen las mismas dimensiones, no se pueden sumar.")
    
    # A × B
    print("A × B:")
    print(np.dot(A, B))

# Llamar a la función
operaciones_matrices()
