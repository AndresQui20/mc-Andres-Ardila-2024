import numpy as np
import matplotlib.pyplot as plt

def linear_regression(X, y):
    """Aplica regresión lineal por mínimos cuadrados a los datos."""
    n = len(X)
    
  
    m = (n * np.sum(X * y) - np.sum(X) * np.sum(y)) / (n * np.sum(X**2) - (np.sum(X))**2)
    b = (np.sum(y) - m * np.sum(X)) / n
    
    return m, b

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
    
    X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([15, 11, 13, 7, 9, 6, 5, 2])
    
   
    if len(X) != len(y):
        raise ValueError("Las dimensiones de X y y deben ser iguales.")

   
    m, b = linear_regression(X, y)

    print(f"Pendiente (m): {m:.2f}")
    print(f"Intersección (b): {b:.2f}")

    
    plot_regression(X, y, m, b)

if __name__ == "__main__":
    main()
