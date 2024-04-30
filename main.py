from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from commission import commission_router
from user import user_router
from payment import payment_router
from portfolio import portfolio_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_index():
    return FileResponse("./frontend/login.html")


app.include_router(commission_router)
app.include_router(user_router)
app.include_router(payment_router)
app.include_router(portfolio_router)

app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
