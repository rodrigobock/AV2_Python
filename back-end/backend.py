from config import *
from models import Pessoa
from models import Disciplina
from models import EstudanteDisciplina

@app.route("/")
def inicio():
    return 'Sistema de cadastro de uma escola. '+\
        '<a href="/listar_pessoas">Operação listar pessoas</a>  <br>' +\
        '<a href="/listar_disciplinas">Operação listar disciplinas</a> <br>' +\
        '<a href="/listar_dp">Operação listar disciplina - estudante </a>' 

@app.route("/listar_pessoas")
def listar_pessoas():
    # obter as pessoas do cadastro
    pessoas = db.session.query(Pessoa).all()
    # aplicar o método json que a classe Pessoa possui a cada elemento da lista
    pessoas_em_json = [ x.json() for x in pessoas ]
    # converter a lista do python para json
    resposta = jsonify(pessoas_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/listar_disciplinas")
def listar_disciplinas():
    # obter as disciplinas
    disciplinas = db.session.query(Disciplina).all()
    # aplicar o método json que a classe Pessoa possui a cada elemento da lista
    d_em_json = [ x.json() for x in disciplinas ]
    # converter a lista do python para json
    resposta = jsonify(d_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/listar_dp")
def listar_dp():
    # obter as disciplinas - estudantes
    dp = db.session.query(EstudanteDisciplina).all()
    # aplicar o método json que a classe Pessoa possui a cada elemento da lista
    dp_em_json = [ x.json() for x in dp ]
    # converter a lista do python para json
    resposta = jsonify(dp_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar..

app.run(debug=True)