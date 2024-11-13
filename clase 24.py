import numpy as np


x_points = np.array([0, 1, 2, 3, 4])
y_points = np.array([1, 0.9, -1, -2.3, 1.8])


def lagrange_interpolation(x_points, y_points, x):
    total_sum = 0
    n = len(x_points)
    
    for i in range(n):
        
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        
        
        total_sum += term
    
    return total_sum


x_value = 2.5
result = lagrange_interpolation(x_points, y_points, x_value)
print(f"El valor interpolado en x = {x_value} es: {result}")
