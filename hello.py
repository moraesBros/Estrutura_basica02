# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def titulo():
    return '<p><h1>Aula 030. Semana 02. Estrutura básica da aplicação.</h1></p>'

@app.route('/home')
def home():
    return 'home'

@app.route('/Identificacao')
def Identificacao():
    return '<p><b><h2>Avaliação contínua: Aula 030</h2></b></p><p><b><h3>Aluno: Ednilton S. Moraes</h3></b></p><p><b><h3>Prontuário: PT3025527</h3></b></p><p><b><h4>Instituição: IFSP</h4></b></p><p><h5>Voltar</h5></p>'

@app.route('/Contexto')
def Contexto():
    return '<p><b><h2>Avaliação contínua: Aula 030</h2></b></p><p><b><h3>Seu navegador é: Mozilla/5.0 (Windows NT 10.0; Win 64; X64) Apple Web Kit/537.36 (KHTML, Like Gecko) Chrome/139.0.0;0</h3></b></p><p><b><h3>O IP do computador remoto é: 10;0;4;170</h3></b></p><p><b><h4>O host da aplicação é: ednilton.pythonanywhere.com</h4></b></p><p><h5>Voltar</h5></p>'

