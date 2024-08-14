Python
def solicitar_CONJUNTO(nombre_conjunto): numeros = input("ingrese los numeros decimales")
conjunto = []
for num in numeros.split():conjunto.append(float(num))

def union(conjunto1, conjunto2):
    resultado = conjunto1.copy()
    for elemento in conjunto2:
        if elemento not in resultado:
            resultado.appened(elemento)
            return resultado
        
def interseccion(conjunto1,conjunto2):
    resultado = []
    for elemnto in conjunto1:
        if elemento in conjunto2:
            resultado.append(elemnto)
            return resultado
        
def diferencia(conjunto1,conjunto2):
    resultado = []
    for elemento in conjunto1:
        if elemento not in conjunto2:
            resultado.append(elemento)
            return resultado
        
def diferencia_simetrica(conjunto1,conjunto2):
    resultado = []
    for elemento in conjunto1:
        if elemento not in conjunto2:
            resultado.append(elemento)
            for elemento in conjunto2:
                if elemento not in conjunto1:
                    resultado.append(elemento)
                    return resultado
                
def main():
    print("Bienvenido al programa de operaciones entre conjuntos de números decimales.")
    
    conjunto1 = solicitar_conjunto("primer conjunto")
    conjunto2 = solicitar_conjunto("segundo conjunto")
    
    print("\nOperaciones disponibles:")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Diferencia Simétrica")
    
    opcion = input("Elija la operación a realizar (escriba el nombre exacto): ").strip().lower()
    
    if opcion == "unión":
        conjunto_resultante = union(conjunto1, conjunto2)
    elif opcion == "intersección":
        conjunto_resultante = interseccion(conjunto1, conjunto2)
    elif opcion == "diferencia":
        conjunto_resultante = diferencia(conjunto1, conjunto2)
    elif opcion == "diferencia simétrica":
        conjunto_resultante = diferencia_simetrica(conjunto1, conjunto2)
    else:
        print("Operación no válida.")
        return
    
    conjunto_resultante = list(dict.fromkeys(conjunto_resultante))  # Eliminar duplicados
    print(f"\nEl conjunto resultante es: {conjunto_resultante}")
    print(f"Su cardinalidad es: {len(conjunto_resultante)}")

if __name__ == "__main__":
    main()



