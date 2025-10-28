# criar as classes para o banco de dados
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

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
    admin = Column("admin", Boolean, default=False)


    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

#Pedido
class Pedido(Base):
    __tablename__ = "pedidos"

    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) # pendente, cancelado, finalizado
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    # itens =

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status

#ItensPedido
class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    qtd = Column("quantidada", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho",String)
    preco_uni = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, qtd, sabor, tamanho, preco_uni, pedido):
        self.qtd = qtd
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_uni = preco_uni
        self.pedido = pedido

#Executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)
