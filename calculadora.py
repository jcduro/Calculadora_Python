import tkinter as tk
from tkinter import messagebox
import math

def agregar(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + valor)

def limpiar():
    entrada.delete(0, tk.END)

def retroceso():
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual[:-1])

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Expresión inválida")

def raiz_cuadrada():
    try:
        valor = float(entrada.get())
        resultado = math.sqrt(valor)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Número inválido para raíz cuadrada")

def porcentaje():
    try:
        expr = entrada.get()
        # Si hay una operación como 650*30
        if "*" in expr:
            partes = expr.split("*")
            if len(partes) == 2:
                base = float(eval(partes[0]))
                porc = float(eval(partes[1])) / 100
                resultado = base * porc
            else:
                raise Exception()
        elif "+" in expr:
            partes = expr.split("+")
            if len(partes) == 2:
                base = float(eval(partes[0]))
                porc = float(eval(partes[1])) / 100
                resultado = base + base * porc
            else:
                raise Exception()
        elif "-" in expr:
            partes = expr.split("-")
            if len(partes) == 2:
                base = float(eval(partes[0]))
                porc = float(eval(partes[1])) / 100
                resultado = base - base * porc
            else:
                raise Exception()
        elif "/" in expr:
            partes = expr.split("/")
            if len(partes) == 2:
                base = float(eval(partes[0]))
                porc = float(eval(partes[1])) / 100
                resultado = base / (porc if porc else 1)
            else:
                raise Exception()
        else:
            # Si no hay operador: solo divide entre 100
            resultado = float(eval(expr)) / 100
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Número u operación inválidos para porcentaje")


ventana = tk.Tk()
ventana.title("Calculadora Python Mejorada")
ventana.config(bg="#23262e")
ventana.resizable(0,0)

entrada = tk.Entry(ventana, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right", bg="#f1f1f1", fg="#23262e")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

botones = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("+",4,2), ("=",4,3),
    ("C",5,0), ("√",5,1), ("%",5,2), ("⌫",5,3),
]
for (texto, fila, columna) in botones:
    if texto == "=":
        b = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 16), command=calcular, bg="#4caf50", fg="white")
    elif texto == "C":
        b = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 16), command=limpiar, bg="#f44336", fg="white")
    elif texto == "√":
        b = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 16), command=raiz_cuadrada, bg="#00897b", fg="white")
    elif texto == "%":
        b = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 16), command=porcentaje, bg="#009688", fg="white")
    elif texto == "⌫":
        b = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 16), command=retroceso, bg="#607d8b", fg="white")
    else:
        b = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 16),
                      command=lambda valor=texto: agregar(valor), bg="#282b33", fg="white")
    b.grid(row=fila, column=columna, padx=5, pady=5)

ventana.mainloop()
