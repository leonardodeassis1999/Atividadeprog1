from sqlalchemy import Column, Integer, String, Date
from database import Base

class Carro(Base):
    __tablename__ = "carro"

    id = Column(Integer, primary_key=True, index=True)
    cor = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    ano = Column(Date, nullable=False)