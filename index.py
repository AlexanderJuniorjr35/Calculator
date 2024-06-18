import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            result = "Operação inválida!"
        
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora")

# Variáveis
operation_var = tk.StringVar(value='+')
result_var = tk.StringVar()

# Estilo
root.configure(padx=40, pady=40, bg="black")

# Layout
tk.Label(root, text="Primeiro número:", bg="black", fg="white").grid(row=0, column=0, pady=5)
entry1 = tk.Entry(root, width=15)
entry1.grid(row=0, column=1, pady=5)

tk.Label(root, text="Segundo número:", bg="black", fg="white").grid(row=1, column=0, pady=5)
entry2 = tk.Entry(root, width=15)
entry2.grid(row=1, column=1, pady=5)

tk.Label(root, text="Operação:", bg="black", fg="white").grid(row=2, column=0, pady=5)
tk.OptionMenu(root, operation_var, '+', '-', '*', '/').grid(row=2, column=1, pady=5)

tk.Button(root, text="Calcular", command=calculate, bg="red", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(root, text="Resultado:", bg="#24f222").grid(row=4, column=0, pady=5)
tk.Entry(root, textvariable=result_var, state='readonly', width=20).grid(row=4, column=1, pady=5)

# Iniciar a aplicação
root.mainloop()
