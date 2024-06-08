from fastapi import FastAPI, HTTPException

#creamos el crud
#agregamos 
from db import session
from models.todo import Todo

app = FastAPI()

#para bd es async
@app.post("/")
async def create_todo(text: str, is_done: bool = False):
    todo = Todo(text=text, is_done=is_done)
    session.add(todo)
    session.commit()
    return {"todo added": todo.text}

@app.get("/")
def root():
    return {"message": "Hola, mi nombre es Nathalia Maria Orozco"}