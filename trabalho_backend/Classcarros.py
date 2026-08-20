from sqlalchemy import Column,String,Integer,Date
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Carro (base):
    __tablename__ = "carro"
    id = Column (Integer,primary_key=True, index = True)
    cor = Column(String(50),nullable=False)
    modelo = Column (String(50), nullable=False)
    ano = Column(Date, nullable=False)