from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

modelo = pickle.load(open("modelo.pkl", "rb"))

# ROTA WEB (continua igual)
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    
    if request.method == "POST":
        hora = float(request.form["hora"])
        entrada = pd.DataFrame([[hora]], columns=["hora"])
        previsao = modelo.predict(entrada)
        resultado = round(previsao[0], 2)

    return render_template("index.html", resultado=resultado)


# 🔥 NOVA ROTA API (ESSA É A CHAVE DA SPRINT 4)
@app.route("/prever", methods=["POST"])
def prever():
    dados = request.get_json()
    
    hora = float(dados["hora"])
    
    entrada = pd.DataFrame([[hora]], columns=["hora"])
    previsao = modelo.predict(entrada)
    
    return jsonify({
        "ruido_previsto": round(float(previsao[0]), 2)
    })

app.run(debug=True)