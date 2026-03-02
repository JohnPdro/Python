from conexao_orm import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base) : # Cria uma tabela, Base é necessário para dizer que a classe é uma tabela
    __tablename__ = 'users' # Dá nome a tabela, caso esteja vazio puxa o nome da classe

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    posts = relationship('Post', back_populates='author')

    def __init__(self, name, email) :
        self.name = name
        self.email = email