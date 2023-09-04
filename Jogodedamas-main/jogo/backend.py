# importações
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from config import *
from resultado import Resultado

# rota para retornar o Resultado
@app.route("/")
def ola():
    return "backend operante"

# curl localhost:5000/listar_resultado

@app.route("/listar_resultado")
def listar_resultado():
    try:
        # obter os dados
        lista = db.session.query(Resultado).all()
        # converter pra json
        lista_retorno = [x.json() for x in lista]
        # preparar uma parte da resposta: resultado ok
        meujson = {"Resultado": "ok"}
        meujson.update({"detalhes": lista_retorno})
        # retornar a lista de pessoas json, com resultado ok
        resposta = jsonify(meujson)
        return resposta
    except Exception as e:
        return jsonify({"Resultado": "erro", "detalhes": str(e)})

# iniciar o backend (app.run)
with app.app_context():

    # criar o banco de dados, caso não esteja criado
    db.create_all()

    # provendo o CORS ao sistema
    CORS(app)

    # iniciar o servidor
    app.run(debug=True)
