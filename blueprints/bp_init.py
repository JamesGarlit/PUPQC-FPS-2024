from flask import Flask
from blueprints.web.configurations.auth import auth_bp
from blueprints.web.configurations.executives import exec_bp

def blueprint_start():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config['SECRET_KEY'] = 'pup-qc_fps'
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(exec_bp)
    
    return app
