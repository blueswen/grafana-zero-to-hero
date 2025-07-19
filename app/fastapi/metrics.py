import time

import uvicorn
from fastapi import FastAPI, Request
from prometheus_client import Counter, Gauge, disable_created_metrics, make_asgi_app

app = FastAPI()
app.mount("/metrics", make_asgi_app())

# Disable unused created series for counters, histograms, and summaries Ref: https://prometheus.github.io/client_python/instrumenting/#disabling-_created-metrics
disable_created_metrics()

REQUEST_COUNT = Counter("requests_count", "Total count of requests")
STATUS_INFO = Gauge("status_info", "Status information", ["status"])


@app.get("/")
async def root(request: Request):
    REQUEST_COUNT.inc()
    current_step = int(time.time() // 60) % 5
    STATUS_INFO.clear()
    if current_step <= 1:
        STATUS_INFO.labels(status="on").set(1)
    elif current_step <= 3:
        STATUS_INFO.labels(status="off").set(1)
    else:
        STATUS_INFO.labels(status="unknown").set(1)
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
