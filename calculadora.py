import tkinter as tk
from tkinter import messagebox
import math

def seno(x):
    resultado = 0.0
    for n in range(10):
        signo = (-1) ** n
        resultado += signo * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return resultado

def coseno(x):
    resultado = 0.0
    for n in range(10):
        signo = (-1) ** n
        resultado += signo * (x ** (2 * n)) / math.factorial(2 * n)
    return resultado

def tangente(x):
    return seno(x) / coseno(x)

def secante(x):
    return 1 / coseno(x)

def cosecante(x):
    return 1 / seno(x)

def cotangente(x):
    return coseno(x) / seno(x)

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora Trigonométrica")
        self.master.geometry("400x300")
        self.master.config(bg="#f0f0f0")
        
        self.label = tk.Label(master, text="Ingrese la expresión:", font=("Arial", 14), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 12), width=30, borderwidth=2, relief="groove")
        self.entry.pack(pady=5)

        self.calculate_button = tk.Button(master, text="Calcular", command=self.calculate, font=("Arial", 12), bg="#4CAF50", fg="white", activebackground="#45a049")
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 12), bg="#f0f0f0")
        self.result_label.pack(pady=10)

    def calculate(self):
        expression = self.entry.get()
        try:
            result = eval(self.parse_expression(expression))
            self.result_label.config(text=f"Resultado: {result:.8f}")
        except Exception as e:
            self.result_label.config(text="Error")
            messagebox.showerror("Error", str(e))

    def parse_expression(self, expression):
        expression = expression.replace("sen", "seno")
        expression = expression.replace("cos", "coseno")
        expression = expression.replace("tan", "tangente")
        expression = expression.replace("sec", "secante")
        expression = expression.replace("csc", "cosecante")
        expression = expression.replace("cot", "cotangente")
        return expression

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
