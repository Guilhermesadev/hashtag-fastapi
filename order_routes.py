from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/") # aqui eu passo o decorator
async def pedidos():
    return {"mensagem" : "Voce acessou a rota de pedidos"}
