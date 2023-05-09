from flask import Flask
from custom_logger import get_logger
from app.main import main_bp
from app.errors import errors_bp
from app.auth import auth_bp


logger = get_logger(sreaming=True, name='INIT_APP')

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(errors_bp)

    logger.info('Instance is created!')

    return app