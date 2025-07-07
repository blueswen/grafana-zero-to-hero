import asyncio
import logging
import os
import random
import time

import uvicorn
from fastapi import FastAPI, Request, Response
from utils import PrometheusMiddleware, metrics
import pyroscope
import httpx
from fastapi import HTTPException

APP_NAME = os.environ.get("APP_NAME", "app")
EXPOSE_PORT = os.environ.get("EXPOSE_PORT", 8000)
ENABLE_PYROSCOPE = os.environ.get("ENABLE_PYROSCOPE", "false").lower() == "true"
PYROSCOPE_SERVER = os.environ.get("PYROSCOPE_SERVER", "http://localhost:4040")

TARGET_ONE_SVC = os.environ.get("TARGET_ONE_SVC", f"localhost:{EXPOSE_PORT}")
TARGET_TWO_SVC = os.environ.get("TARGET_TWO_SVC", f"localhost:{EXPOSE_PORT}")

app = FastAPI()
app.add_middleware(PrometheusMiddleware, app_name=APP_NAME)
app.add_route("/metrics", metrics)

if ENABLE_PYROSCOPE:
    pyroscope.configure(
        application_name = "fastapi",
        server_address   = PYROSCOPE_SERVER, # replace this with the address of your Pyroscope server
        tags             = {
            "app_name": APP_NAME,
        }
    )

def time_effect():
    return time.time() % 180 // 60 % 3


@app.get("/")
async def root(request: Request):
    """
    Hello World
    """
    return {"Hello": "World"}


@app.get("/io_task")
async def io_task():
    """
    IO task simulation with sleep
    """
    await asyncio.sleep(time_effect())
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
    if response.status_code == 200:
        await asyncio.sleep(random.randint(1, 3) * time_effect())
    logging.error("random status")
    return {"path": "/random_status"}


@app.get("/random_sleep")
async def random_sleep(response: Response):
    """
    Random sleep time endpoint
    """
    await asyncio.sleep(random.randint(0, 5) * time_effect())
    logging.error("random status")
    return {"path": "/random_status"}


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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(EXPOSE_PORT))
