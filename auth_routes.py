from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# dominio/auth/
@auth_router.get("/")
async def autenticar():
    """
    Rota padrão de autenticação # Docs string
    """
    return {"mensagem": "Voce acessou a rota padrao de autenticação", "autenticação": False}

