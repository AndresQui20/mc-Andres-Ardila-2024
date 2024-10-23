import numpy as np
import matplotlib.pyplot as plt

def linear_regression(X, y):
    """Aplica regresión lineal por mínimos cuadrados a los datos."""
    n = len(X)
    
    
    m = (n * np.sum(X * y) - np.sum(X) * np.sum(y)) / (n * np.sum(X**2) - (np.sum(X))**2)
    b = (np.sum(y) - m * np.sum(X)) / n
    
    return m, b

def calculate_statistics(X, y, m, b):
    """Calcula la desviación estándar, error estándar, r y R^2."""
    n = len(X)
    
    
    y_pred = m * X + b
    
    
    sy = np.sqrt(np.sum((y - np.mean(y))**2) / (n - 1))
    
    
    se = np.sqrt(np.sum((y - y_pred)**2) / (n - 2))
    
    
    r = np.corrcoef(X, y)[0, 1]
    
    
    r_squared = r**2
    
    return sy, se, r, r_squared, y_pred

def print_data_table(X, y, y_pred):
    """Imprime una tabla con los datos originales y las predicciones."""
    print("\nTabla de datos:")
    print(f"{'X':<10}{'y':<10}{'y_pred':<10}")
    print("-" * 30)
    for x, actual, predicted in zip(X, y, y_pred):
        print(f"{x:<10}{actual:<10.2f}{predicted:<10.2f}")

def plot_regression(X, y, m, b):
    """Grafica los datos y la línea de regresión."""
    y_pred = m * X + b
    
    plt.scatter(X, y, color='blue', label='Datos originales')
    plt.plot(X, y_pred, color='red', label='Línea ajustada')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Regresión Lineal por Mínimos Cuadrados')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    
    X = np.array([1, 2, 3, 4, 5, 6, 7])
    y = np.array([0.1, 0.3, 0.9, 1.7, 2.8, 4.5, 6.9])
    
    if len(X) != len(y):
        raise ValueError("Las dimensiones de X y y deben ser iguales.")
    
    m, b = linear_regression(X, y)
    sy, se, r, r_squared, y_pred = calculate_statistics(X, y, m, b)
    
    print(f"Pendiente (m): {m:.2f}")
    print(f"Intersección (b): {b:.2f}")
    print(f"Desviación estándar (sy): {sy:.2f}")
    print(f"Error estándar de la estimación (se): {se:.2f}")
    print(f"Coeficiente de correlación (r): {r:.2f}")
    print(f"Coeficiente de determinación (R^2): {r_squared:.2f}")
    
    print_data_table(X, y, y_pred) 
    
    plot_regression(X, y, m, b)

if __name__ == "__main__":
    main()
