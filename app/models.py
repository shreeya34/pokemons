from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    image_url = Column(String)
    type = Column(String, index=True)
