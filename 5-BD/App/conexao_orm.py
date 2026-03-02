# Importa a função responsável por criar a conexão com o banco de dados
from sqlalchemy import create_engine

# Importa a ferramenta que cria sessões para interagir com o banco
from sqlalchemy.orm import sessionmaker

# Importa a classe base usada para criar modelos (tabelas) no estilo ORM
from sqlalchemy.ext.declarative import declarative_base


# ==============================
# CONFIGURAÇÃO DE CONEXÃO
# ==============================

# Usuário do banco de dados
user = 'postgres'

# Senha do banco
password = '123456'

# Endereço do servidor (localhost = sua própria máquina)
host = 'localhost'

# Nome do banco de dados
database = 'blog'


# String de conexão no formato aceito pelo SQLAlchemy
# postgresql://usuario:senha@host/nome_do_banco
DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'


# ==============================
# CRIAÇÃO DO ENGINE
# ==============================

# O engine é o objeto que gerencia a conexão com o banco
# Ele é responsável por enviar comandos SQL para o banco
engine = create_engine(DATABASE_URI)


# ==============================
# CRIAÇÃO DA SESSÃO
# ==============================

# sessionmaker cria uma "fábrica de sessões"
# bind=engine conecta essa fábrica ao banco configurado
Session = sessionmaker(bind=engine)

# Aqui criamos uma instância da sessão
# A sessão é usada para fazer operações como:
# - inserir dados
# - consultar dados
# - atualizar
# - deletar
session = Session()


# ==============================
# BASE PARA MODELOS ORM
# ==============================

# Base é a classe base que será herdada por todas as tabelas (modelos)
# Cada classe criada a partir dela representará uma tabela no banco
Base = declarative_base()