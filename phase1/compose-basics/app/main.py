from fastapi import FastAPI
import os
import redis

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
r = redis.from_url(REDIS_URL, decode_responses=True)

app = FastAPI(title="DevOps Learning API")

@app.get("/healthz")
def healthz():
    try:
        r.ping()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.get("/")
def index():
    hits = r.incr("hits")
    return {
        "message": "Hello from FastAPI + Docker!",
        "hits": hits
    }
