from fastapi import Request, HTTPException
from time import time

rate_limit_store = {}
RATE_LIMIT = 5
WINDOW = 60

async def rate_limiter(request: Request):
    ip = request.client.host
    now = time()
    history = rate_limit_store.get(ip, [])
    history = [t for t in history if now - t < WINDOW]

    if len(history) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    history.append(now)
    rate_limit_store[ip] = history

