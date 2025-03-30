import json
import os
from itertools import combinations

# FUNCIONES DE PERSISTENCIA (AQUÍ VA EL CÓDIGO QUE AGREGAMOS)
def guardar_elementos(elementos, archivo="elementos.json"):
    """Guarda los elementos en un archivo JSON"""
    with open(archivo, "w") as f:
        json.dump(elementos, f, indent=4)

def cargar_elementos(archivo="elementos.json"):
    """Carga los elementos desde un archivo JSON si existe"""
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            return json.load(f)
    return []

def ingresar_elementos():
    """Función para que el usuario ingrese elementos o cargue desde JSON"""
    elementos = cargar_elementos()
    
    if elementos:
        print("\n📂 Se encontraron elementos guardados. ¿Deseas usarlos? (s/n)")
        usar_guardados = input("-> ").strip().lower()
        if usar_guardados == "s":
            return elementos
    
    elementos = []
    while True:
        try:
            n = int(input("¿Cuántos elementos deseas ingresar? "))
            if n <= 0:
                print("El número de elementos debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    for i in range(n):
        nombre = input(f"Ingrese el nombre del elemento {i+1}: ").strip()
        while True:
            try:
                peso = float(input(f"Ingrese el peso de {nombre}: ").strip())
                if peso <= 0:
                    print("El peso debe ser mayor a 0.")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el peso.")

        while True:
            try:
                calorias = float(input(f"Ingrese las calorías de {nombre}: ").strip())
                if calorias <= 0:
                    print("Las calorías deben ser mayores a 0.")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para las calorías.")

        elementos.append({"nombre": nombre, "peso": peso, "calorias": calorias})
    
    guardar_elementos(elementos)
    return elementos

# FUNCIONES PRINCIPALES (NO CAMBIAN)
def encontrar_mejor_combinacion(elementos, min_calorias, peso_maximo):
    """Función para encontrar la mejor combinación de elementos"""
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

    return mejores_combinaciones, mejor_peso, mejor_calorias

def imprimir_resultado(mejores_combinaciones, mejor_peso, mejor_calorias):
    """Función para imprimir el resultado de la mejor combinación"""
    if mejores_combinaciones:
        print("\n✅ Mejor combinación encontrada:")
        for combinacion in mejores_combinaciones:
            nombres = [elemento['nombre'] for elemento in combinacion]
            print(f"Elementos: {', '.join(nombres)}")
            print(f"Peso total: {mejor_peso:.2f} kg")
            print(f"Calorías totales: {mejor_calorias:.2f}\n")
    else:
        print("\n❌ No hay una combinación válida.")

def main():
    """Función principal"""
    print("🔹 PROGRAMA DE OPTIMIZACIÓN DE ELEMENTOS 🔹")

    elementos = ingresar_elementos()

    while True:
        try:
            min_calorias = float(input("Ingrese el mínimo de calorías necesarias: "))
            if min_calorias <= 0:
                print("El mínimo de calorías debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    while True:
        try:
            peso_maximo = float(input("Ingrese el peso máximo permitido: "))
            if peso_maximo <= 0:
                print("El peso máximo debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    mejores_combinaciones, mejor_peso, mejor_calorias = encontrar_mejor_combinacion(elementos, min_calorias, peso_maximo)

    imprimir_resultado(mejores_combinaciones, mejor_peso, mejor_calorias)

if __name__ == "__main__":
    main()

