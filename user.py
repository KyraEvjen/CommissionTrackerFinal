import os
from fastapi import security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBasicCredentials
import jwt

# from jose import JWTError
from dotenv import load_dotenv
from fastapi import APIRouter, Body, HTTPException, status, Depends
from model import User
from passlib.context import CryptContext
from datetime import datetime, timedelta
from user_manager import UserManager

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = os.getenv("SECRET_KEY")


def generate_token(username: str) -> str:
    token_expiry = datetime.utcnow() + timedelta(hours=1)  # Token expires in 1 hour
    payload = {"username": username, "exp": token_expiry}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    print("Token Generated:" + token)
    return token


# Function to hash a password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# Function to verify a password against its hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


user_router = APIRouter()
user_manager = UserManager()

from pymongo import MongoClient

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)


db = client["CommissionTracker"]
users_collection = db["users"]

if "users" not in db.list_collection_names():
    db.create_collection("users")


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if not (user := user.authenticate_user(credentials.username, credentials.password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user["username"]


# User authentication dependency
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends()):
    if credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid authentication scheme",
        )

    if not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization credentials not provided",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username: str = payload.get("username")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: missing username",
                headers={"WWW-Authenticate": "Bearer"},
            )
        # Here you would typically fetch the user from the database using the username
        # For demonstration purposes, we'll assume you have a UserManager class
        user_manager = UserManager()
        user = await user_manager.get_user_by_username(username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        print("Found User get_current_user:")
        return user
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def is_admin(current_user: User = Depends(get_current_username)):
    if current_user and current_user.is_admin:
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action.",
        )


# async def get_current_user(user: User = Depends(UserManager.authenticate_user)):
#     if user:
#         return user
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )


@user_router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@user_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: User):

    existing_user = await user_manager.get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    user_id = await user_manager.create_user(user)

    return {"message": "User created successfully", "user_id": user_id}


@user_router.post("/login")
async def login(username: str = Body(...), password: str = Body(...)):
    print("Received login request with username:", username)
    print("Received login request with password:", password)

    # Authenticate the user with the provided username and password
    authenticated_user = await user_manager.authenticate_user(username, password)

    if authenticated_user:
        token = generate_token(username)
        return {
            "message": "Login successful",
            "username": username,
            "token": token,
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
