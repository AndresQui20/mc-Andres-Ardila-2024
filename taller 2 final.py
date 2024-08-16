def ingresar_conjunto(nombre):
    elementos = input(f"Ingrese los elementos del conjunto {nombre} separados por comas: ")
    conjunto = set(elementos.split(','))
    return conjunto

# Solicitar los conjuntos U y A
conjunto_U = ingresar_conjunto("U (Conjunto Universal)")
conjunto_A = ingresar_conjunto("A")

# Verificar que A sea subconjunto de U
if conjunto_A.issubset(conjunto_U):
    print("\nA es un subconjunto de U. Realizando operaciones...\n")
    
    # (U ∪ A) ∩ A
    union_interseccion = (conjunto_U.union(conjunto_A)).intersection(conjunto_A)
    print(f"(U ∪ A) ∩ A = {union_interseccion}")

    # (U ∩ A) ⨁ A
    interseccion_simetrica = (conjunto_U.intersection(conjunto_A)).symmetric_difference(conjunto_A)
    print(f"(U ∩ A) ⨁ A = {interseccion_simetrica}")

    # (U - A) ⨁ A
    diferencia_simetrica = (conjunto_U.difference(conjunto_A)).symmetric_difference(conjunto_A)
    print(f"(U - A) ⨁ A = {diferencia_simetrica}")
else:
    print("\nA no es un subconjunto de U. No se pueden realizar las operaciones.")
