import json
import logging
import os
import random
import time
from typing import List

import httpx
import redis
import uvicorn
import pyroscope
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from todo_app import crud, models, schemas
from todo_app.database import SessionLocal, engine
from utils import PrometheusMiddleware, metrics, setting_otlp

APP_NAME = os.environ.get("APP_NAME", "app")
EXPOSE_PORT = os.environ.get("EXPOSE_PORT", 8000)
REDIS_SERVER = os.environ.get("REDIS_SERVER", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
TIME_BOMB = os.environ.get("TIME_BOMB", "false").lower().strip() == "true"
CODE_BASED_INSTRUMENTATION = (
    os.environ.get("CODE_BASED_INSTRUMENTATION", "false").lower().strip() == "true"
)
ENABLE_PYROSCOPE = os.environ.get("ENABLE_PYROSCOPE", "false").lower() == "true"
PYROSCOPE_SERVER = os.environ.get("PYROSCOPE_SERVER", "http://localhost:4040")

TARGET_ONE_SVC = os.environ.get("TARGET_ONE_SVC", f"localhost:{EXPOSE_PORT}")
TARGET_TWO_SVC = os.environ.get("TARGET_TWO_SVC", f"localhost:{EXPOSE_PORT}")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Setting metrics middleware
app.add_middleware(PrometheusMiddleware, app_name=APP_NAME)
app.add_route("/metrics", metrics)

if CODE_BASED_INSTRUMENTATION:
    setting_otlp(app, APP_NAME, os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT"))

if ENABLE_PYROSCOPE:
    pyroscope.configure(
        application_name = "fastapi",
        server_address   = PYROSCOPE_SERVER, # replace this with the address of your Pyroscope server
        tags             = {
            "app_name": APP_NAME,
        }
    )


class EndpointFilter(logging.Filter):
    # Uvicorn endpoint access log filter
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find("GET /metrics") == -1


# Filter out /endpoint
logging.getLogger("uvicorn.access").addFilter(EndpointFilter())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


r = redis.Redis(host=REDIS_SERVER, port=int(REDIS_PORT), db=0)


def store_todo_in_redis(key, json_data, expire_time=10):
    # Serialize the JSON data
    json_str = json.dumps(json_data)
    # Store the serialized JSON string in Redis
    r.setex(key, expire_time, json_str)


def read_todo_from_redis(key):
    # Retrieve the JSON string from Redis
    json_str = r.get(key)
    if json_str is None:
        return None
    # Deserialize the JSON string
    return json.loads(json_str)


def delete_todo_from_redis(key):
    r.delete(key)


@app.get("/")
async def root(request: Request):
    """
    Root endpoint with logging
    """
    logging.info(f"Request headers: {request.headers}")
    logging.debug("Debugging log")
    logging.info("Info log")
    logging.warning("Hey, This is a warning!")
    logging.error("Oops! We have an Error. OK")
    logging.critical("Critical error. Please fix this!")
    return {"Hello": "World"}


@app.get("/io_task")
async def io_task():
    """
    IO task simulation with sleep
    """
    time.sleep(1)
    logging.error("io task")
    return "IO bound task finish!"


@app.get("/cpu_task")
async def cpu_task():
    """
    CPU task simulation with calculation
    """
    for i in range(1000):
        _ = i * i * i
    logging.error("cpu task")
    return "CPU bound task finish!"


@app.get("/random_status")
async def random_status(response: Response):
    """
    Random status code endpoint
    """
    response.status_code = random.choice([200, 201, 300, 400, 500])
    logging.error("random status")
    return {"path": "/random_status"}


@app.get("/random_sleep")
async def random_sleep(response: Response):
    """
    Random sleep time endpoint
    """
    time.sleep(random.randint(0, 5))
    logging.error("random sleep")
    return {"path": "/random_sleep"}


@app.get("/chain")
async def chain(response: Response):
    """
    Chain of requests
    """
    logging.info("Chain Start")
    async with httpx.AsyncClient() as client:
        await client.get(
            "http://localhost:8000/",
        )
    async with httpx.AsyncClient() as client:
        await client.get(
            f"http://{TARGET_ONE_SVC}/io_task",
        )
    async with httpx.AsyncClient() as client:
        await client.get(
            f"http://{TARGET_TWO_SVC}/cpu_task",
        )
    logging.info("Chain End")
    return {"path": "/chain"}


@app.get("/error")
def error():
    """
    Error endpoint
    """
    logging.critical("Critical error. Please fix this!")
    raise HTTPException(status_code=500, detail="This is an error")


@app.post("/todos/", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    """
    Create a new Todo item
    """
    todo_item = crud.create_todo(db, todo)
    store_todo_in_redis(str(todo_item.id), todo_item.to_dict())
    logging.error(f"Create todo: {todo_item.id}")
    return todo_item


@app.get("/todos/{todo_id}", response_model=schemas.Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    Read a Todo item
    """
    todo_item = read_todo_from_redis(str(todo_id))
    if todo_item:
        logging.error(f"Read todo: {todo_id} from cache")
        return todo_item
    todo_item = crud.get_todo(db, todo_id)
    if todo_item is None:
        logging.error(f"Read todo: {todo_id} not found")
        raise HTTPException(status_code=404, detail="Todo not found")
    logging.error(todo_item.to_dict())
    store_todo_in_redis(str(todo_id), todo_item.to_dict())
    logging.error(f"Read todo: {todo_id}")
    return todo_item


@app.put("/todos/{todo_id}", response_model=schemas.Todo)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    """
    Update a Todo item
    """

    todo_item = crud.update_todo(db, todo_id, todo)
    store_todo_in_redis(str(todo_id), todo_item.to_dict())
    logging.error(f"Update todo: {todo_id}")
    return todo_item


@app.delete("/todos/{todo_id}", response_model=schemas.Todo)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    Delete a Todo item
    """
    todo_item = crud.delete_todo(db, todo_id)
    delete_todo_from_redis(str(todo_id))
    logging.error(f"Delete todo: {todo_id}")
    return todo_item


@app.get("/todos/", response_model=List[schemas.Todo])
def list_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    List Todo items
    """
    # Trigger an delay if TIME_BOMB is set and every 50th second to 60th second every minute
    if TIME_BOMB and 50 <= time.localtime().tm_sec < 60:
        time.sleep(random.randint(3, 5))
        logging.error("Gotcha! Time bomb triggered")
    todo_item_list = crud.get_todo_list(db, skip, limit)
    logging.error(f"Get todo list length: {len(todo_item_list)}")
    return todo_item_list


if __name__ == "__main__":
    log_config = uvicorn.config.LOGGING_CONFIG
    if CODE_BASED_INSTRUMENTATION:
        fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s resource.service.name=%(otelServiceName)s] - %(message)s"
        log_config["formatters"]["access"]["fmt"] = fmt
        log_config["formatters"]["default"]["fmt"] = fmt
    uvicorn.run(app, host="0.0.0.0", port=int(EXPOSE_PORT), log_config=log_config)
