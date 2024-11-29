from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///exemplo.db"
    with app.app_context(): #criar o banco de acordo com o app
        db.init_app(app)
        db.create_all()