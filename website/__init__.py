from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from website.attrs import DB_NAME, PORTFOLIO_EMAIL, PORTFOLIO_PASSWORD

db = SQLAlchemy()


def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    application = Flask(__name__, static_folder="static")
    application.config["SECRET_KEY"] = "alsdchauwhcww9e"
    application.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    application.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
    application.config["MAIL_SERVER"] = "smtp.gmail.com"
    application.config["MAIL_PORT"] = 587
    application.config["MAIL_USERNAME"] = PORTFOLIO_EMAIL
    application.config["MAIL_PASSWORD"] = PORTFOLIO_PASSWORD
    application.config["MAIL_USE_TLS"] = True
    application.config["MAIL_USE_SSL"] = False
    application.config["MAIL_DEFAULT_SENDER"] = PORTFOLIO_EMAIL
    db.init_app(application)

    with application.app_context():
        if not path.exists("website/" + DB_NAME):
            db.create_all()

    from .views import views_blueprint
    from .topics import topics_blueprint
    from .articles import articles_blueprint

    application.register_blueprint(views_blueprint, url_prefix="/")
    application.register_blueprint(topics_blueprint, url_prefix="/topics")
    application.register_blueprint(articles_blueprint, url_prefix="/topics")

    return application

    return application
