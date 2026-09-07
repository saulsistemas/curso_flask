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
@app.route('/')
def inicio():
    return 'Hola Mundo'

#5 - if __name__ == "__main__" Esta es una característica propia de Python
if __name__ == "__main__":
    app.run(debug=True)
