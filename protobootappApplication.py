from flask import Flask, request, jsonify
from calculadora import Calculadora

app = Flask(__name__)
calculadora = Calculadora()

@app.route('/')
def index():
    return "Bienvenido! Esta aplicación ayuda a elevar números cualquiera a sus potencias."

@app.route('/hola')
def hola():
    nombre = request.args.get('nombre', 'Mundo')
    return f"Hola {nombre}!"

@app.route('/cuadrado')
def cuadrado():
    numero = request.args.get('numero', default=0, type=float)
    resultado = calculadora.cuadrado(numero)
    return f"El cuadrado de {numero} es {resultado}"

@app.route('/cubo')
def cubo():
    numero = request.args.get('numero', default=0, type=float)
    resultado = calculadora.cubo(numero)
    return f"El cubo de {numero} es {resultado}"

if __name__ == '__main__':
    app.run(port=5000)
