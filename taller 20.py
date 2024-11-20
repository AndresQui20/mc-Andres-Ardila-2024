import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2.2, 3.3, 3.7, 4.0, 4.2, 4.4, 4.5, 4.7])

# 1. Modelo de línea recta: y = mx + b
def linear_regression(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, b = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, b

# 2. Modelo exponencial: y = a * e^(bx)
def exponential_regression(x, y):
    log_y = np.log(y)
    m, b = linear_regression(x, log_y)
    a = np.exp(b)
    return a, m

# 3. Modelo de ecuación de potencias: y = a * x^b
def power_regression(x, y):
    log_x = np.log(x)
    log_y = np.log(y)
    b, log_a = linear_regression(log_x, log_y)
    a = np.exp(log_a)
    return a, b

# 4. Modelo de razón de crecimiento: y = a / (1 + b * e^(-kx))
def growth_ratio_regression(x, y):
    from scipy.optimize import curve_fit
    def growth_model(x, a, b, k):
        return a / (1 + b * np.exp(-k * x))
    params, _ = curve_fit(growth_model, x, y, p0=[5, 1, 0.1])
    return params

# Ajuste de los modelos
m, b = linear_regression(x, y)
a_exp, b_exp = exponential_regression(x, y)
a_pow, b_pow = power_regression(x, y)
a_gr, b_gr, k_gr = growth_ratio_regression(x, y)

# Predicciones
x_fit = np.linspace(min(x), max(x), 100)
y_linear = m * x_fit + b
y_exponential = a_exp * np.exp(b_exp * x_fit)
y_power = a_pow * x_fit**b_pow
y_growth = a_gr / (1 + b_gr * np.exp(-k_gr * x_fit))

# Gráficas
plt.figure(figsize=(12, 8))

plt.scatter(x, y, color='black', label='Datos originales')
plt.plot(x_fit, y_linear, label=f'Línea recta: y = {m:.2f}x + {b:.2f}', color='blue')
plt.plot(x_fit, y_exponential, label=f'Exponencial: y = {a_exp:.2f}e^({b_exp:.2f}x)', color='green')
plt.plot(x_fit, y_power, label=f'Potencias: y = {a_pow:.2f}x^{b_pow:.2f}', color='orange')
plt.plot(x_fit, y_growth, label=f'Razón crecimiento: y = {a_gr:.2f} / (1 + {b_gr:.2f}e^(-{k_gr:.2f}x))', color='red')

plt.title("Ajuste de los diferentes modelos", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
