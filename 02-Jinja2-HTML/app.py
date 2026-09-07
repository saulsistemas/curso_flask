from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensaje')
def mensaje():
    nombre = 'Sandro'
    amigos=['Juan','carlos','migel']
    return render_template('mensaje.html', nombreHtml = nombre, amigosHtml=amigos)


if __name__ == '__main__':
    app.run(debug=True)