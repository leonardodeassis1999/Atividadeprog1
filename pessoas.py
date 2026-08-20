from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import  declarative_base
base = declarative_base()




class pessoas (base):
    __tablename__ = "pessoas"
    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String(100),nullable=False)
    cidade = Column(String(100),nullable=False)