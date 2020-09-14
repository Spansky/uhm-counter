from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

counter = 0

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

counters = APIRouter()

class Counter(BaseModel):
    counter: int

@counters.get('/', response_model=Counter)
async def index():
    return {"counter": counter}

@counters.post('/reset', response_model=Counter)
async def reset():
    global counter
    counter = 0
    return {"counter": counter}


@counters.post('/increment', response_model=Counter)
async def increment():
    global counter
    counter += 1
    return {"counter": counter}

app.include_router(counters, prefix='', tags=['counters'])
