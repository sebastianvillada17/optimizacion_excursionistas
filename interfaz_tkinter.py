import tkinter as tk
from tkinter import messagebox
from itertools import combinations
import json
import csv

elementos = []

def cargar_datos():
    """Carga los elementos desde un archivo JSON"""
    global elementos
    try:
        with open("elementos.json", "r") as file:
            elementos = json.load(file)
            for e in elementos:
                lista_elementos.insert(tk.END, f"{e['nombre']} - Peso: {e['peso']} kg, Calorías: {e['calorias']}")
    except FileNotFoundError:
        elementos = []

def guardar_datos():
    """Guarda los elementos en un archivo JSON"""
    with open("elementos.json", "w") as file:
        json.dump(elementos, file)

def exportar_csv():
    """Exporta los resultados a un archivo CSV"""
    with open("resultados.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Peso (kg)", "Calorías"])
        for e in elementos:
            writer.writerow([e["nombre"], e["peso"], e["calorias"]])
    messagebox.showinfo("Exportación exitosa", "Los datos han sido exportados a resultados.csv")

def agregar_elemento():
    nombre = entry_nombre.get()
    try:
        peso = float(entry_peso.get())
        calorias = float(entry_calorias.get())
        if peso <= 0 or calorias <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos para peso y calorías.")
        return
    
    elementos.append({"nombre": nombre, "peso": peso, "calorias": calorias})
    lista_elementos.insert(tk.END, f"{nombre} - Peso: {peso} kg, Calorías: {calorias}")
    guardar_datos()
    entry_nombre.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_calorias.delete(0, tk.END)

def encontrar_mejor_combinacion():
    try:
        min_calorias = float(entry_min_calorias.get())
        peso_maximo = float(entry_peso_max.get())
        if min_calorias <= 0 or peso_maximo <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos para restricciones.")
        return
    
    mejores_combinaciones = []
    mejor_peso = float('inf')
    mejor_calorias = 0
    
    for r in range(1, len(elementos) + 1):
        for combinacion in combinations(elementos, r):
            peso_total = sum(e["peso"] for e in combinacion)
            calorias_total = sum(e["calorias"] for e in combinacion)
            
            if calorias_total >= min_calorias and peso_total <= peso_maximo:
                if peso_total < mejor_peso:
                    mejor_peso = peso_total
                    mejor_calorias = calorias_total
                    mejores_combinaciones = [combinacion]
                elif peso_total == mejor_peso:
                    mejores_combinaciones.append(combinacion)
                    mejor_calorias = max(mejor_calorias, calorias_total)
    
    if mejores_combinaciones:
        resultado = "\n\n✅ Mejor combinación encontrada:\n"
        for combinacion in mejores_combinaciones:
            nombres = [e['nombre'] for e in combinacion]
            resultado += f"Elementos: {', '.join(nombres)}\nPeso total: {mejor_peso:.2f} kg\nCalorías totales: {mejor_calorias:.2f}\n"
        messagebox.showinfo("Resultado", resultado)
    else:
        messagebox.showerror("Sin solución", "No hay una combinación válida.")

# Crear ventana principal
root = tk.Tk()
root.title("Optimización de Elementos")
root.geometry("400x550")

# Campos de entrada
tk.Label(root, text="Nombre del Elemento:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Peso (kg):").pack()
entry_peso = tk.Entry(root)
entry_peso.pack()

tk.Label(root, text="Calorías:").pack()
entry_calorias = tk.Entry(root)
entry_calorias.pack()

tk.Button(root, text="Agregar Elemento", command=agregar_elemento).pack()

# Lista de elementos
lista_elementos = tk.Listbox(root, width=50)
lista_elementos.pack()

# Ahora sí, después de definir lista_elementos, llamamos a cargar_datos()
cargar_datos()

# Campos de restricción
tk.Label(root, text="Mínimo de Calorías:").pack()
entry_min_calorias = tk.Entry(root)
entry_min_calorias.pack()

tk.Label(root, text="Peso Máximo (kg):").pack()
entry_peso_max = tk.Entry(root)
entry_peso_max.pack()

tk.Button(root, text="Optimizar", command=encontrar_mejor_combinacion).pack()

tk.Button(root, text="Exportar a CSV", command=exportar_csv).pack()

root.mainloop()
import tkinter as tk
from tkinter import messagebox
from itertools import combinations
import json
import csv

elementos = []

def cargar_datos():
    """Carga los elementos desde un archivo JSON"""
    global elementos
    try:
        with open("elementos.json", "r") as file:
            elementos = json.load(file)
            for e in elementos:
                lista_elementos.insert(tk.END, f"{e['nombre']} - Peso: {e['peso']} kg, Calorías: {e['calorias']}")
    except FileNotFoundError:
        elementos = []

def guardar_datos():
    """Guarda los elementos en un archivo JSON"""
    with open("elementos.json", "w") as file:
        json.dump(elementos, file)

def exportar_csv():
    """Exporta los resultados a un archivo CSV"""
    with open("resultados.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Peso (kg)", "Calorías"])
        for e in elementos:
            writer.writerow([e["nombre"], e["peso"], e["calorias"]])
    messagebox.showinfo("Exportación exitosa", "Los datos han sido exportados a resultados.csv")

def agregar_elemento():
    nombre = entry_nombre.get()
    try:
        peso = float(entry_peso.get())
        calorias = float(entry_calorias.get())
        if peso <= 0 or calorias <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos para peso y calorías.")
        return
    
    elementos.append({"nombre": nombre, "peso": peso, "calorias": calorias})
    lista_elementos.insert(tk.END, f"{nombre} - Peso: {peso} kg, Calorías: {calorias}")
    guardar_datos()
    entry_nombre.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_calorias.delete(0, tk.END)

def encontrar_mejor_combinacion():
    try:
        min_calorias = float(entry_min_calorias.get())
        peso_maximo = float(entry_peso_max.get())
        if min_calorias <= 0 or peso_maximo <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos para restricciones.")
        return
    
    mejores_combinaciones = []
    mejor_peso = float('inf')
    mejor_calorias = 0
    
    for r in range(1, len(elementos) + 1):
        for combinacion in combinations(elementos, r):
            peso_total = sum(e["peso"] for e in combinacion)
            calorias_total = sum(e["calorias"] for e in combinacion)
            
            if calorias_total >= min_calorias and peso_total <= peso_maximo:
                if peso_total < mejor_peso:
                    mejor_peso = peso_total
                    mejor_calorias = calorias_total
                    mejores_combinaciones = [combinacion]
                elif peso_total == mejor_peso:
                    mejores_combinaciones.append(combinacion)
                    mejor_calorias = max(mejor_calorias, calorias_total)
    
    if mejores_combinaciones:
        resultado = "\n\n✅ Mejor combinación encontrada:\n"
        for combinacion in mejores_combinaciones:
            nombres = [e['nombre'] for e in combinacion]
            resultado += f"Elementos: {', '.join(nombres)}\nPeso total: {mejor_peso:.2f} kg\nCalorías totales: {mejor_calorias:.2f}\n"
        messagebox.showinfo("Resultado", resultado)
    else:
        messagebox.showerror("Sin solución", "No hay una combinación válida.")

# Crear ventana principal
root = tk.Tk()
root.title("Optimización de Elementos")
root.geometry("400x550")

# Campos de entrada
tk.Label(root, text="Nombre del Elemento:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Peso (kg):").pack()
entry_peso = tk.Entry(root)
entry_peso.pack()

tk.Label(root, text="Calorías:").pack()
entry_calorias = tk.Entry(root)
entry_calorias.pack()

tk.Button(root, text="Agregar Elemento", command=agregar_elemento).pack()

# Lista de elementos
lista_elementos = tk.Listbox(root, width=50)
lista_elementos.pack()

# Ahora sí, después de definir lista_elementos, llamamos a cargar_datos()
cargar_datos()

# Campos de restricción
tk.Label(root, text="Mínimo de Calorías:").pack()
entry_min_calorias = tk.Entry(root)
entry_min_calorias.pack()

tk.Label(root, text="Peso Máximo (kg):").pack()
entry_peso_max = tk.Entry(root)
entry_peso_max.pack()

tk.Button(root, text="Optimizar", command=encontrar_mejor_combinacion).pack()

tk.Button(root, text="Exportar a CSV", command=exportar_csv).pack()

root.mainloop()
