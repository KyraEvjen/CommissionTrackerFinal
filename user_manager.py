import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from model import User
from security import hash_password, verify_password

# MongoDB connection settings
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)


myDatabase = client["CommissionTracker"]
users_collection = myDatabase["users"]


class UserManager:
    def __init__(self):
        self.client = AsyncIOMotorClient(mongo_uri)
        self.db = self.client["CommissionTracker"]
        self.collection = self.db["users"]

    async def create_user(self, user: User):
        # print("Received user data:", user.dict())
        user_data = user.dict()
        user_data["password"] = hash_password(user_data["password"])
        result = await self.collection.insert_one(user_data)
        # print("Inserted user ID:", str(result.inserted_id))
        return str(result.inserted_id)

    async def get_user_by_username(self, username: str):
        user_data = await self.collection.find_one({"username": username})
        return user_data

    async def authenticate_user(self, username: str, password: str):

        try:
            user_data = await self.get_user_by_username(username)
            if user_data:
                hashed_password = user_data.get("password")
                if hashed_password and verify_password(password, hashed_password):
                    return User(**user_data)
        except Exception as e:
            print(f"An error occurred during user authentication: {e}")
        return None
