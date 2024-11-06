import numpy as np


data = np.array([
    [1, 0, 1.2],
    [1, 0.5, 4],
    [2, 0.5, 0.2],
    [3, 1, 0.6],
    [1, 1, 4.5],
    [2, 1.5, 4.6],
    [3, 1.5, 1.5],
    [3, 0.5, -2]
])


x1 = data[:, 0]
x2 = data[:, 1]
y = data[:, 2]


X = np.column_stack((np.ones(len(x1)), x1, x2))

beta = np.linalg.inv(X.T @ X) @ X.T @ y


beta_0, beta_1, beta_2 = beta


y_pred = X @ beta


mean_x1 = np.mean(x1)
mean_x2 = np.mean(x2)
mean_y = np.mean(y)

numerator = np.sum((x1 - mean_x1) * (y - mean_y)) + np.sum((x2 - mean_x2) * (y - mean_y))
denominator = np.sqrt(np.sum((x1 - mean_x1)**2) * np.sum((y - mean_y)**2)) + np.sqrt(np.sum((x2 - mean_x2)**2) * np.sum((y - mean_y)**2))

r = numerator / denominator


print(f"Coeficientes de la regresión lineal:")
print(f"β0 (intercepto) = {beta_0}")
print(f"β1 (coeficiente de x1) = {beta_1}")
print(f"β2 (coeficiente de x2) = {beta_2}")
print(f"\nCoeficiente de correlación (r) = {r}")
