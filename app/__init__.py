from flask import Flask


def create_app():
    app = Flask(__name__)

    # Load configuration from config.py if needed
    # app.config.from_pyfile('config.py')

    # Register blueprints and other configurations here
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
