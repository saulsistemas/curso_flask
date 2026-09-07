#1 Importa la clase Flask desde el paquete Flask, es decir "Traeme la herramienta Flask para crear mi aplicación web"
from flask import Flask

#2 - Creando un objeto Flask, Constructor de Flask, Le indica a Flask cuál es el archivo principal.
#2.1 - app es una variable que almacena nuestra aplicación.
#Podríamos llamarla: mi_web = Flask(__name__), Pero por convención casi todos usan: app
#2.2 - __name__  indica donde esta el archivo principal , le estas diciendo a flask "Flask, usa este archivo como punto de partida." 
#print(__name__)

app = Flask(__name__)

#3 - Decorador @ , el decorador va con el objeto que se creo para instanciar la clase Flask(), en este caso app
#3.1 - utilizar el metodo route para URL
#3.2 - Podemos acceder desde distintas rutas a una funcion en especifica
@app.route('/')
@app.route('/index') 
def inicio():
    return 'Hola Mundo'

#3.3 - retornar un html
@app.route('/contacto')
def contacto():
    return '<h1>pagina de contacto</h1>'

#3.4 enviar valores mediante url de tipo string por defecto http://127.0.0.1:5000/hola/juan
@app.route('/hola/<name>')
def hola(name):
    return f'<h1>Hola mundo {name} </h1>'

#3.4 enviar valores mediante url de tipo int http://127.0.0.1:5000/adios/1
@app.route('/adios/<int:name>')
def adios(name:int):
    return f'<h1>Adiós mundo {name} </h1>'

#3.4 enviar 2 valores mediante url de tipo string int http://127.0.0.1:5000/saludo/juan/25
@app.route('/saludo/<name>/<int:edad>')
def saludo(name,edad:int):
    return f'<h1>Hola {name} y tu edad es {edad} </h1>'

#3.5 enviar n valores mediante varias rutas de tipo string int 
#http://127.0.0.1:5000/mensaje
#http://127.0.0.1:5000/mensaje/juan
#http://127.0.0.1:5000/mensaje/juan/15

@app.route('/mensaje')
@app.route('/mensaje/<name>')
@app.route('/mensaje/<name>/<int:edad>')
def mensaje(name = None,edad= None):
    if name == None and edad == None:
        return '<h1>Hola Mundo</h1>'
    elif edad == None:
        return f'<h1>Hola mundo {name} </h1>'
    else:
        return f'<h1>Hola {name} y tu edad es {edad} </h1>'

#evitando ataque de inyeccion http://127.0.0.1:5000/code/%3Cscript%3Ealert('hola')%3C/script%3E
from markupsafe import escape
@app.route('/code/<path:code>') 
def code(code):
    return f'<code>{ escape(code)}  </code>'

#5 - if __name__ == "__main__" Esta es una característica propia de Python
if __name__ == "__main__":
    app.run(debug=True)
