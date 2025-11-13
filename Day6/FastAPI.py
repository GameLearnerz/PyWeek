from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

todos = [Todo(id=1, title="Clean The Bed", completed=False),
         Todo(id=2, title="Write Code", completed=False),
         Todo(id=3, title="Read Book", completed=False)
         ]

@app.post("/todos")
def create_todos(task: str):
    new_id= len(todos) + 1
    new_todo = Todo(id=new_id, title=task, completed=False)
    todos.append(new_todo)
    return new_todo

@app.get("/todos")
def view_todos():
    return list(todos)

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: str):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index].title = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            delete_todo = todos.pop(index)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")

