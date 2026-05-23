from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import pickle
import pandas as pd

app = Flask(__name__)

# =========================
# CONFIG POSTGRESQL
# =========================

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/devopsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# =========================
# MODELO IA
# =========================

modelo = pickle.load(open("modelo.pkl", "rb"))

# =========================
# TABELA CURSO
# =========================

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

# =========================
# TABELA ALUNO
# =========================

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'))

# =========================
# HOME WEB
# =========================

@app.route("/", methods=["GET", "POST"])
def index():

    resultado = None

    if request.method == "POST":

        hora = float(request.form["hora"])

        entrada = pd.DataFrame([[hora]], columns=["hora"])

        previsao = modelo.predict(entrada)

        resultado = round(previsao[0], 2)

    return render_template("index.html", resultado=resultado)

# =========================
# API IA
# =========================

@app.route("/prever", methods=["POST"])
def prever():

    dados = request.get_json()

    hora = float(dados["hora"])

    entrada = pd.DataFrame([[hora]], columns=["hora"])

    previsao = modelo.predict(entrada)

    return jsonify({
        "ruido_previsto": round(float(previsao[0]), 2)
    })

# =========================
# CRUD CURSOS
# =========================

@app.route("/cursos", methods=["POST"])
def criar_curso():

    data = request.json

    curso = Curso(nome=data["nome"])

    db.session.add(curso)
    db.session.commit()

    return jsonify({
        "msg": "Curso criado com sucesso!"
    })

@app.route("/cursos", methods=["GET"])
def listar_cursos():

    cursos = Curso.query.all()

    resultado = []

    for curso in cursos:

        resultado.append({
            "id": curso.id,
            "nome": curso.nome
        })

    return jsonify(resultado)

# =========================
# CRUD ALUNOS
# =========================

@app.route("/alunos", methods=["POST"])
def criar_aluno():

    data = request.json

    aluno = Aluno(
        nome=data["nome"],
        curso_id=data["curso_id"]
    )

    db.session.add(aluno)
    db.session.commit()

    return jsonify({
        "msg": "Aluno criado com sucesso!"
    })

@app.route("/alunos", methods=["GET"])
def listar_alunos():

    alunos = Aluno.query.all()

    resultado = []

    for aluno in alunos:

        resultado.append({
            "id": aluno.id,
            "nome": aluno.nome,
            "curso_id": aluno.curso_id
        })

    return jsonify(resultado)

# =========================
# START APP
# =========================

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=5000)