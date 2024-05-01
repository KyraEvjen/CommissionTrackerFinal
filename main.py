import uvicorn
import json
import logging
from logging_setup import setup_logging
from typing import Any
from fastapi import FastAPI, status, APIRouter, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from functools import lru_cache
from beanie import init_beanie, PydanticObjectId
from starlette.responses import FileResponse
from commission import commission_router
from portfolio import portfolio_router
from payment import payment_router
from pydantic import BaseModel, Field
from model import CommissionRequest
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings, SettingsConfigDict


app = FastAPI()

setup_logging()
logger = logging.getLogger(__name__)


app.add_middleware(

    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def read_index():
    return FileResponse("./frontend/index.html")

#@app.get("/")
#async def read_pfindex():
#    return FileResponse("./frontend/portfolio.html")

app.include_router(commission_router)
app.include_router(portfolio_router)
app.include_router(payment_router)

app.mount("/", StaticFiles(directory="frontend"), name="static")

# uvicorn.run(app, host="localhost", port=8000)
