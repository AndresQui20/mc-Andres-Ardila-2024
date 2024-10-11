import copy

def imprimirSistema(a, b, etiqueta):
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print("|", b[i])
    print()

def gaussJordan(ao, bo):
    a = copy.deepcopy(ao)
    b = copy.copy(bo)

    n = len(b)
    imprimirSistema(a, b, "Matriz inicial")
    for i in range(n):
        pivote = a[i][i]

        # Dividir por el pivote
        for j in range(n):
            a[i][j] /= pivote
        b[i] /= pivote
        imprimirSistema(a, b, "División")

        # Reducción
        for k in range(n):
            if i != k:
                # Se reduce
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                b[k] += b[i] * valorAux
        imprimirSistema(a, b, "Reducción")
    
    return b

# Definición del sistema de ecuaciones
a = [[1, 0, 1],    # x1 + x3 = 5
     [3, 4, 3],    # 3x1 + 4x2 + 3x3 = 23
     [4, 1, 0]]    # 4x1 + x2 = 30
b = [5, 23, 30]

# Resolver el sistema
x = gaussJordan(a, b)

# Mostrar la respuesta
print("Respuesta:")
for i in range(len(x)):
    print("x" + str(i + 1), "=", x[i])

# Pruebas
print("\nPruebas:")
for i in range(len(b)):
    valorAux = b[i]
    for j in range(len(b)):
        valorAux -= a[i][j] * x[j]
    print("Test", i + 1, "=", valorAux)
