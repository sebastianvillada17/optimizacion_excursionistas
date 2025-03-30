from flask import Flask, render_template, request, jsonify
from itertools import combinations

app = Flask(__name__)

# Función para encontrar la mejor combinación
def encontrar_mejor_combinacion(elementos, min_calorias, peso_maximo):
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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    elementos = data.get("elementos", [])
    min_calorias = data.get("min_calorias", 0)
    peso_maximo = data.get("peso_maximo", 0)

    mejores_combinaciones, mejor_peso, mejor_calorias = encontrar_mejor_combinacion(elementos, min_calorias, peso_maximo)

    return jsonify({
        "mejores_combinaciones": mejores_combinaciones,
        "mejor_peso": mejor_peso,
        "mejor_calorias": mejor_calorias
})

if __name__ == "__main__":
    app.run(debug=True)