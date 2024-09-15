import asyncio
import logging
import os
import random
import time

import uvicorn
from fastapi import FastAPI, Request, Response
from utils import PrometheusMiddleware, metrics

APP_NAME = os.environ.get("APP_NAME", "app")
EXPOSE_PORT = os.environ.get("EXPOSE_PORT", 8000)

app = FastAPI()
app.add_middleware(PrometheusMiddleware, app_name=APP_NAME)
app.add_route("/metrics", metrics)


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
    await asyncio.sleep(1) * time_effect()
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
    response.status_code = random.choice([200, 200, 300, 400, 500])
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=EXPOSE_PORT)
