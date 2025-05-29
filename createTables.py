# create_tables.py
from app import app, db # Supondo que 'app' é sua instância Flask e 'db' é SQLAlchemy em app.py
import os

# Carrega variáveis de ambiente do sistema
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_ENDPOINT = os.environ.get('DB_ENDPOINT')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT', '5432')

if not all([DB_USERNAME, DB_PASSWORD, DB_ENDPOINT, DB_NAME]):
    print("ERRO CRÍTICO: Variáveis de ambiente do banco de dados não estão configuradas para criar tabelas.")
    exit(1) # Sai do script se as variáveis não estiverem definidas

# Configura a URI do banco de dados para o contexto deste script
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    try:
        print(f"Tentando conectar ao banco: postgresql://{DB_USERNAME}:****@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}")
        db.create_all()
        print("Tabelas criadas com sucesso no RDS!")
    except Exception as e:
        print(f"Falha ao criar tabelas: {e}")