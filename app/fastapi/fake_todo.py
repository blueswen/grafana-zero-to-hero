import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel

TODO_LIST = [
    {
        "id": 1,
        "title": "Buy groceries",
        "completed": False,
        "factor": 1.2,
        "details": {"location": "supermarket", "executor": "John"},
    },
    {
        "id": 2,
        "title": "Clean room",
        "completed": True,
        "factor": 1.5,
        "details": {"location": "home", "executor": "Jane"},
    },
    {
        "id": 3,
        "title": "Play games",
        "completed": False,
        "factor": 1.8,
        "details": {"location": "home", "executor": "John"},
    },
]


class Query(BaseModel):
    completed: bool


app = FastAPI()


# RESTful API
@app.get("/")
async def root(request: Request):
    """
    Hello World
    """
    return {"Hello": "World"}


@app.get("/todo")
async def get_todo_list():
    """
    Get todo list
    """
    return TODO_LIST


@app.get("/todo/{todo_id}")
async def get_todo_by_id(todo_id: int):
    """
    Get todo by id
    """
    return TODO_LIST[todo_id - 1]


@app.post("/todo")
async def create_todo(todo: dict):
    """
    Create todo
    """
    TODO_LIST.append(todo)
    return {"message": "Todo created!"}


@app.put("/todo/{todo_id}")
async def update_todo(todo_id: int, todo: dict):
    """
    Update todo
    """
    TODO_LIST[todo_id - 1] = todo
    return {"message": "Todo updated!"}


@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
    """
    Delete todo
    """
    del TODO_LIST[todo_id - 1]
    return {"message": "Todo deleted!"}


# Post query
@app.post("/query")
async def post_query(query: Query):
    """
    Post query
    """
    return [todo for todo in TODO_LIST if todo["completed"] == query.completed]


@app.get("/nested")
async def get_nested():
    """
    Get nested
    """
    return {"app_name": "Todo List", "todos": TODO_LIST}


@app.get("/executor_json")
async def get_executor():
    """
    Get executor
    """
    data = {}
    for todo in TODO_LIST:
        executor = todo["details"]["executor"]
        if executor not in data:
            data[executor] = []
        data[executor].append(todo)
    return data


@app.get("/executor_name_list")
async def get_executor_name_list():
    """
    Get executor name list
    """
    return list(set([todo["details"]["executor"] for todo in TODO_LIST]))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
