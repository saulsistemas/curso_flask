from flask import Flask, render_template,request

def create_app():
    
    app = Flask(__name__)

    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG       = True,
        SECRET_KEY = 'dev'
    )
    
    #registro de Blueprint
    from . import todo
    app.register_blueprint(todo.bp)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    @app.route('/')
    def index():
        return 'hola mundo'

    return app