from app import create_app, db  

app = create_app() 

def init_db():
    with app.app_context():
        db.create_all()  

if __name__ == '__main__':
    init_db()
    print("Banco de dados inicializado com sucesso!")
