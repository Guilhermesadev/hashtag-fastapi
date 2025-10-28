# criar as classes para o banco de dados
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# Criar a conexão com o banco
db = create_engine("sqlite:///banco.db")

#Cria a base do banco de dados
Base = declarative_base()

#Criar as classes/tabelas do banco
#Usuario
class Usuario(Base):
    __tablename__ = "usuarios" # defini o nome da tabela

    id = Column("id", Integer, primary_key=True, autoincrement=True )
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean)


#Pedido
#ItensPedido
#Executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)
