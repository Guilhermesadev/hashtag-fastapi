from fastapi import FastAPI #importa

app = FastAPI() #Extanciar o fastapi

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

# Rodar no terminal o comando "uvicorn nome_arquivo:app --reload"

# GET = leitura/pegar
# POST = enviar/criar
# PUT/PATCH = edição
# DELETE = deletar


