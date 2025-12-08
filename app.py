from flask import Flask, jsonify, abort
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # permite llamadas

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SALIDAS_DIR = os.path.join(BASE_DIR, "salidas")

def leer_csv(nombre_archivo):
    path = os.path.join(SALIDAS_DIR, nombre_archivo)
    if not os.path.exists(path):
        abort(404, description=f"Archivo no encontrado: {path}") # devolvemos 404 con mensaje claro
    df = pd.read_csv(path)
    return df

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "mensaje": "API funcionando. Endpoints disponibles: /roi, /correlaciones, /runtime, /rating_idioma"
    })

@app.route("/roi", methods=["GET"])
def roi():
    df = leer_csv("roi_por_genero.csv")
    return jsonify(df.to_dict(orient="records"))

@app.route("/correlaciones", methods=["GET"])
def correlaciones():
    df = leer_csv("correlaciones_budget_rating.csv")
    return jsonify(df.to_dict(orient="records"))

@app.route("/runtime", methods=["GET"])
def runtime():
    df = leer_csv("promedio_runtime_50anios.csv")
    return jsonify(df.to_dict(orient="records"))

@app.route("/rating_idioma", methods=["GET"])
def rating_idioma():
    df = leer_csv("rating_por_idioma.csv")
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True) # esto permite correr: python app.py