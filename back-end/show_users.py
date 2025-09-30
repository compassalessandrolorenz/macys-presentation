import os
from app import create_app, db
from models.user import User

# Cria uma instância da aplicação para ter o contexto correto
app = create_app()

with app.app_context():
    # Verifica se o arquivo do banco de dados existe
    db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')
    if not os.path.exists(db_path):
        print("O banco de dados 'app.db' ainda não foi criado.")
        print("Por favor, execute o 'app.py' primeiro para criar o banco de dados e a tabela.")
    else:
        try:
            users = User.query.all()
            if not users:
                print("Nenhum usuário cadastrado no banco de dados.")
            else:
                print("--- Usuários Cadastrados ---")
                for user in users:
                    print(f"ID: {user.id}")
                    print(f"Nome: {user.name}")
                    print(f"Email: {user.email}")
                    print(f"Ativo: {user.active}")
                    print(f"Criado em: {user.created_at}")
                    print("-" * 20)
        except Exception as e:
            print(f"Ocorreu um erro ao acessar o banco de dados: {e}")
            print("É possível que a tabela 'users' ainda não exista.")
            print("Por favor, execute o 'app.py' primeiro.")

