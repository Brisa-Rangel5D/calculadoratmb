from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    edad = int(request.form['edad'])
    genero = request.form['genero']
    actividad = float(request.form['actividad'])

    if genero == 'Hombre':
        tmb = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.75 * edad)
    else:
        tmb = 655.1 + (9.563 * peso) + (1.850 * altura) - (4.676 * edad)

    get = tmb * actividad

    return render_template('resultados.html', tmb=tmb, get=get)

if __name__ == '__main__':
    app.run(debug=True)
