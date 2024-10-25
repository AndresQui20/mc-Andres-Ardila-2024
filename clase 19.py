import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([0.8, 1.2, 1.7, 2.2, 3.2, 4.5])


Y = np.log(y)

n = len(x)
sum_x = np.sum(x)
sum_Y = np.sum(Y)
sum_xy = np.sum(x * Y)
sum_x2 = np.sum(x ** 2)


b = (n * sum_xy - sum_x * sum_Y) / (n * sum_x2 - sum_x ** 2)
A = (sum_Y - b * sum_x) / n


a = np.exp(A)


print(f"Modelo exponencial ajustado: y = {a:.4f} * e^({b:.4f}x)")


plt.scatter(x, y, label='Datos originales', color='blue')
plt.plot(x, a * np.exp(b * x), label='Curva ajustada', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste de Modelo Exponencial')
plt.legend()
plt.show()
