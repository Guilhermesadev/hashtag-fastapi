from os import access

from fastapi import APIRouter, Depends, HTTPException
from models import Usuario, db
from dependencies import pegar_sessao
from main import bcrypt_context
from sqlalchemy.orm import sessionmaker, session
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def criar_token(id_usuario):
    token = f"abcdefghijklmnopqrstuvwxyz{id_usuario}"
    return token

# dominio/auth/
@auth_router.get("/")
async def home():
    """
    Rota padrão de autenticação # Docs string
    """
    return {"mensagem": "Voce acessou a rota padrao de autenticação", "autenticação": False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        # ja existe um usuario com esse email
        raise HTTPException(status_code=400, detail=f"E-mail do usuário já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"Usuario cadastrado com sucesso {usuario_schema.email}"}

    session.close()

    # JWT

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==login_schema.email).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")
    else:
        access_token = criar_token(usuario.id)
        return {
            "access_token": access_token,
                "token_type": "Bearer"
        }
