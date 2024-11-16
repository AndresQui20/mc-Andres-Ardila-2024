import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from scipy import stats

def obtener_datos():
    """
    Recibe los datos de los puntos ingresados por el usuario.
    """
    puntos_raw = puntos_text.get("1.0", "end-1c").strip()
    if puntos_raw:
        try:
            puntos = puntos_raw.split('\n')
            puntos = [tuple(map(float, p.split(','))) for p in puntos]
            return np.array(puntos)
        except ValueError:
            messagebox.showerror("Error", "Formato de datos incorrecto. Use el formato (x,y) en cada línea.")
            return None
    else:
        messagebox.showerror("Error", "Por favor, ingrese al menos un punto.")
        return None

def regresion_lineal(x, y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    y_pred = slope * x + intercept
    residuals = y - y_pred
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_res / ss_tot)
    return slope, intercept, r_squared, std_err, residuals, y_pred

def modelo_exponencial(x, y):
    log_y = np.log(y)
    slope, intercept = np.polyfit(x, log_y, 1)
    a = np.exp(intercept)
    b = slope
    y_pred = a * np.exp(b * x)
    residuals = y - y_pred
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_res / ss_tot)
    std_err = np.sqrt(np.sum(residuals**2) / len(x))
    return a, b, r_squared, std_err, residuals, y_pred

def ecuacion_potencias(x, y):
    log_x = np.log(x)
    log_y = np.log(y)
    slope, intercept = np.polyfit(log_x, log_y, 1)
    a = np.exp(intercept)
    b = slope
    y_pred = a * x**b
    residuals = y - y_pred
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_res / ss_tot)
    std_err = np.sqrt(np.sum(residuals**2) / len(x))
    return a, b, r_squared, std_err, residuals, y_pred

def razon_de_crecimiento(x, y):
    """
    Calcula la razón de crecimiento promedio entre los valores consecutivos de y.
    """
    if len(y) < 2:
        return 0
    ratio = y[1:] / y[:-1]  # Razón entre cada par de puntos consecutivos
    avg_ratio = np.mean(ratio)
    return avg_ratio

def regresion_polinomial(x, y, grado=2):
    coef = np.polyfit(x, y, grado)
    p = np.poly1d(coef)
    y_pred = p(x)
    residuals = y - y_pred
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_res / ss_tot)
    std_err = np.sqrt(np.sum(residuals**2) / len(x))
    return p, r_squared, std_err, residuals, y_pred

def graficar(x, y, y_pred, tipo_modelo):
    plt.scatter(x, y, color='red', label="Puntos originales")
    plt.plot(x, y_pred, label=f"Modelo {tipo_modelo}")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title(f'Regresión {tipo_modelo}')
    plt.show()

def mostrar_resultados():
    datos = obtener_datos()
    if datos is None:
        return
    
    x = datos[:, 0]
    y = datos[:, 1]
    
    # Regresión Lineal
    slope, intercept, r_squared, std_err, residuals, y_pred = regresion_lineal(x, y)
    messagebox.showinfo("Regresión Lineal", f"Función: y = {slope:.2f}x + {intercept:.2f}\n"
                                             f"R²: {r_squared:.2f}\n"
                                             f"Desviación estándar de y: {np.std(y):.2f}\n"
                                             f"Error estándar de la aproximación: {std_err:.2f}")
    graficar(x, y, y_pred, "Lineal")
    
    # Modelo Exponencial
    a, b, r_squared, std_err, residuals, y_pred = modelo_exponencial(x, y)
    messagebox.showinfo("Modelo Exponencial", f"Función: y = {a:.2f} * exp({b:.2f}x)\n"
                                              f"R²: {r_squared:.2f}\n"
                                              f"Desviación estándar de y: {np.std(y):.2f}\n"
                                              f"Error estándar de la aproximación: {std_err:.2f}")
    graficar(x, y, y_pred, "Exponencial")
    
    # Ecuación de Potencias
    a, b, r_squared, std_err, residuals, y_pred = ecuacion_potencias(x, y)
    messagebox.showinfo("Ecuación de Potencias", f"Función: y = {a:.2f} * x^{b:.2f}\n"
                                                  f"R²: {r_squared:.2f}\n"
                                                  f"Desviación estándar de y: {np.std(y):.2f}\n"
                                                  f"Error estándar de la aproximación: {std_err:.2f}")
    graficar(x, y, y_pred, "Potencias")
    
    # Razón de Crecimiento
    ratio = razon_de_crecimiento(x, y)
    messagebox.showinfo("Razón de Crecimiento", f"Razón promedio de crecimiento: {ratio:.2f}")
    
    # Regresión Polinomial de Grado 2
    p, r_squared, std_err, residuals, y_pred = regresion_polinomial(x, y)
    messagebox.showinfo("Regresión Polinomial de Grado 2", f"Función: y = {p[0]:.2f}x² + {p[1]:.2f}x + {p[2]:.2f}\n"
                                                          f"R²: {r_squared:.2f}\n"
                                                          f"Desviación estándar de y: {np.std(y):.2f}\n"
                                                          f"Error estándar de la aproximación: {std_err:.2f}")
    graficar(x, y, y_pred, "Polinomial de Grado 2")

def mostrar_instrucciones():
    """
    Muestra un cuadro de diálogo con instrucciones para ingresar los puntos.
    """
    instrucciones = """Introduce los puntos de la siguiente manera:

1. Cada punto debe estar en formato (x,y), separados por comas.
2. Los puntos deben estar en líneas separadas.
Ejemplo:

(1,2)
(2,4)
(3,6)

Asegúrate de ingresar al menos 5 puntos.
"""
    messagebox.showinfo("Instrucciones", instrucciones)

# Interfaz gráfica usando Tkinter
root = Tk()
root.title("Regresiones por Mínimos Cuadrados")

# Botón de Instrucciones
instrucciones_button = Button(root, text="Instrucciones", command=mostrar_instrucciones)
instrucciones_button.pack(pady=10)

# Entrada de puntos
Label(root, text="Introduce los puntos en formato (x,y) por línea").pack(pady=5)
puntos_text = Text(root, height=10, width=30)
puntos_text.pack(pady=5)
puntos_text.insert(END, "(1,2)\n(2,4)\n(3,6)\n(4,8)\n(5,10)")  # Ejemplo predefinido

# Botón para calcular las regresiones
calcular_button = Button(root, text="Calcular Regresiones", command=mostrar_resultados)
calcular_button.pack(pady=10)

root.mainloop()
