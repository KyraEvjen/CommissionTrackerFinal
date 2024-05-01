import logging
from logging_setup import setup_logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from commission import commission_router
from portfolio import portfolio_router
from payment import payment_router


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


app.include_router(commission_router)
app.include_router(portfolio_router)
app.include_router(payment_router)

app.mount("/", StaticFiles(directory="frontend"), name="static")
