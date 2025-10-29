from fastapi import APIRouter, Depends
from models import Usuario, db
from dependencies import pegar_sessao
from main import bcrypt_context
from sqlalchemy.orm import sessionmaker, session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# dominio/auth/
@auth_router.get("/")
async def home():
    """
    Rota padrão de autenticação # Docs string
    """
    return {"mensagem": "Voce acessou a rota padrao de autenticação", "autenticação": False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        # ja existe um usuario com esse email
        return {"mensagem": "Ja existe um usuario com esse email"}
    else:
        senha_criptografada = bcrypt_context.hash(senha[:72])
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "Usuario cadastrado com sucesso"}

    session.close()