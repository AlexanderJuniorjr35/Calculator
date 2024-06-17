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

# Layout
tk.Label(root, text="Primeiro número:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Segundo número:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Operação:").grid(row=2, column=0)
tk.OptionMenu(root, operation_var, '+', '-', '*', '/').grid(row=2, column=1)

tk.Button(root, text="Calcular", command=calculate).grid(row=3, column=0, columnspan=2)

tk.Label(root, text="Resultado:").grid(row=4, column=0)
tk.Entry(root, textvariable=result_var, state='readonly').grid(row=4, column=1)

# Iniciar a aplicação
root.mainloop()
