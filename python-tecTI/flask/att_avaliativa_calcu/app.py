import requests
from flask import Flask,render_template as rt
from calcular import calcular

app = Flask(__name__)

@app.route("/")
def index():
    return rt("calculadora.html", etapas = '', resultados = '')


@app.route("/calcular", methods = ['POST'])
def calcular_route():
    return calcular()
    

if __name__ == "__main__":
    app.run(
        debug=True
    ) 

