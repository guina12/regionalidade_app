from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/roteamento_turistico'


    db.init_app(app)

    try:
        with app.app_context():
            db.create_all()  # Cria as tabelas, se não existirem
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

    from .routes import main
    app.register_blueprint(main)

    return app
