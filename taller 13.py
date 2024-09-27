import math

def taylor_series_exp(a, x, n):
    sum_series = 0
    e_a = math.exp(-a)  # e^(-0.4)
    
    for i in range(n + 1):
        term = ((-1) ** i) * e_a / math.factorial(i) * ((x - a) ** i)
        sum_series += term

    return sum_series


a = 0.4
x = 0.405
true_value = math.exp(-x)  # e^(-0.405)


errors = []
for n in range(16):
    estimated_value = taylor_series_exp(a, x, n)
    error = abs((true_value - estimated_value) / true_value) * 100
    errors.append((n, estimated_value, error))


for n, est_value, err in errors:
    print(f"Orden {n}: Estimación = {est_value:.10f}, Error = {err:.10f}%")
