from flask import Flask, render_template,request

def create_app():
    
    app = Flask(__name__)

    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG       = True,
        SECRETE_KEY = 'dev'
    )
    
    @app.route('/')
    def index():
        return 'hola mundo'

    return app