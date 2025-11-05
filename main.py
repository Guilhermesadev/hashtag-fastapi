
from fastapi import FastAPI #importa
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os

from passlib.handlers.bcrypt import bcrypt
from sqlalchemy.util import deprecated

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI() #Extanciar o fastapi

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

# Rodar no terminal o comando "uvicorn nome_arquivo:app --reload"

# GET = leitura/pegar
# POST = enviar/criar
# PUT/PATCH = edição
# DELETE = deletar


