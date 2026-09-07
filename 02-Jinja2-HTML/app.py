from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensaje')
def mensaje():
    nombre = 'Sandro'
    return render_template('mensaje.html', nombreHtml = nombre)


if __name__ == '__main__':
    app.run(debug=True)