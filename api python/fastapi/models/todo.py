from SQLAchemy import Boolean, Column, Integer, String
from SQLAchemy.orm import declarative_base
from db import engine

Base = declarative_base()

class Todo(Base):
        __tablename__ = "todos"
        id = Column(Integer, primary_key = True)
        text = Column(String)
        is_done = Column (Boolean, default= False)

Base.metadata.create_all(engine)
