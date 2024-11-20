def producto_escalar():
    # Solicitar longitud de los vectores
    n = int(input("Ingrese la longitud de los vectores: "))
    
    # Inicializar los vectores
    vector_a = []
    vector_b = []
    
    # Pedir los elementos del primer vector
    print("Ingrese los elementos del primer vector:")
    for i in range(n):
        vector_a.append(float(input(f"Elemento {i+1}: ")))
    
    # Pedir los elementos del segundo vector
    print("Ingrese los elementos del segundo vector:")
    for i in range(n):
        vector_b.append(float(input(f"Elemento {i+1}: ")))
    
    # Calcular el producto escalar
    producto = sum([vector_a[i] * vector_b[i] for i in range(n)])
    
    print(f"El producto escalar de los vectores es: {producto}")

# Llamar a la función
producto_escalar()
