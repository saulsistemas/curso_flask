from flask import Flask, render_template

app = Flask(__name__)
# Filtros personalizados
from datetime import datetime

#registrando funcion como filtro para poder enviarlo a la plnatilla HTML que permite agregarlo en html jinja2
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')
#otra manera registrar
#app.add_template_filter(today,'today')

#Funcion para html
def repite(s,n):
    return s *n

#registrando funcion como filtro para poder enviarlo a la plnatilla HTML
@app.template_global
def repite2(s,n):
    return s *n
#otra manera registrar
#app.template_global(repite2,'repite2')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensaje')
def mensaje():
    nombre = 'Sandro'
    amigos=['Juan','carlos','migel']
    fecha =  datetime.now()
    return render_template(
        'mensaje.html',
        nombreHtml  =   nombre,
        amigosHtml  =   amigos,
        fechaHtml   =   fecha,
        repiteHtml  =   repite,
    )

@app.route('/mensaje2/')
@app.route('/mensaje2/<name>')
@app.route('/mensaje2/<name>/<int:edad>')
def mensaje2(name = None,edad= None):
    mi_data = {
        'name':name,
        'edad':edad
    }
    return render_template('mensaje2.html',mi_data=mi_data)


if __name__ == '__main__':
    app.run(debug=True)