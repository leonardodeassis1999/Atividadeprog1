from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
from Classcarros import Carro

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def listar_Carro():
    session = SessionLocal()
    carro = session.query(Carro).all()
    resultado = [{"id:":i.id, "Cor": i.cor, "modelo": i.modelo, "Ano": i.ano}
             for i in carro]
    return resultado

SessionLocal.close()