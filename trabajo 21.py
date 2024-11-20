import numpy as np

# Datos
x = np.array([1, 3, 5, 7, 9, 11, 13])
y = np.array([14.9, 3.6, -2, -3.6, -2.4, 4.4, 14.4])

# Ajuste del polinomio de segundo grado
# Matriz de diseño para el polinomio de segundo grado
X = np.vstack([x**2, x, np.ones(len(x))]).T

# Resolución del sistema X.T @ X @ coef = X.T @ y
coef = np.linalg.lstsq(X, y, rcond=None)[0]

# Polinomio ajustado
a, b, c = coef
print(f"Polinomio ajustado: y = {a:.4f}x² + {b:.4f}x + {c:.4f}")

# Valores ajustados
y_ajustado = a * x**2 + b * x + c

# Cálculo del coeficiente de correlación (r)
media_y = np.mean(y)
ss_total = np.sum((y - media_y)**2)  # Suma total de cuadrados
ss_residual = np.sum((y - y_ajustado)**2)  # Suma residual de cuadrados
r_cuadrado = 1 - (ss_residual / ss_total)
r = np.sqrt(r_cuadrado)

print(f"Coeficiente de correlación (r): {r:.4f}")
