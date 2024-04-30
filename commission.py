import os
from dotenv import load_dotenv
from fastapi import APIRouter, Path, HTTPException, status, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from model import Commission, CommissionRequest, User
from fastapi.responses import JSONResponse
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from user import get_current_user, is_admin

commission_router = APIRouter()

from pymongo import MongoClient

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["CommissionTracker"]
collection = db["commissions"]
users_collection = db["users"]

if "commissions" not in db.list_collection_names():
    db.create_collection("commissions")

commission_list = []
max_id: int = 0

security = HTTPBasic()


# def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
#     if not (user := authenticate_user(credentials.username, credentials.password)):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Basic"},
#         )
#     return user["username"]


# async def is_admin(username: str):
#     user = await users_collection.find_one({"username": username})
#     if user and user["role"] == "admin":
#         return True
#     return False


@commission_router.post("/commissions", status_code=status.HTTP_201_CREATED)
async def add_commission(commission: CommissionRequest) -> dict:
    # Connect to MongoDB (use your actual connection details)
    clientPost = AsyncIOMotorClient(mongo_uri)
    db = clientPost["CommissionTracker"]
    collectionPost = db["commissions"]

    # Insert the commission into MongoDB
    result = await collectionPost.insert_one(commission.model_dump())
    return {
        "message": "Commission added successfully",
        "item_id": str(result.inserted_id),
    }


@commission_router.get("/commissions")
async def get_commissions() -> dict:
    try:
        data_list = []
        for item in collection.find({}):
            # Include the "_id" field (converted to a string) in the commission data
            item["_id"] = str(item["_id"])
            item["mongodb_id"] = item["_id"]
            data_list.append(Commission(**item))
        return {"commissions": data_list}
    except Exception as e:
        return JSONResponse(content={"error": str(e)})


@commission_router.get(
    "/commissions/{commission_id}", response_description="Get commission by ID"
)
async def get_commission(commission_id: str):
    try:
        print("Getting commission with ID:", commission_id)
        commission_object_id = ObjectId(commission_id)
        commission = collection.find_one({"_id": commission_object_id})
        if commission:
            return CommissionRequest(**commission)
        else:
            raise HTTPException(
                status_code=404, detail=f"Commission with ID {commission_id} not found"
            )
    except Exception as e:
        # Log the error for debugging purposes
        print(f"An error occurred: {e}")

        # Raise an HTTPException with a 500 status code
        raise HTTPException(status_code=500, detail="Internal Server Error")


@commission_router.put(
    "/commissions/{commission_id}", response_description="Update commission by ID"
)
async def update_commission(
    commission_id: str,
    updated_commission: CommissionRequest,
    # current_user: User = Depends(get_current_user),
):
    # if not is_admin(current_user):
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail="You do not have permission to perform this action.",
    #     )
    try:
        # Convert commission_id to ObjectId
        commission_object_id = ObjectId(commission_id)

        # Ensure that the commission_id exists in the database
        existing_commission = collection.find_one({"_id": commission_object_id})
        if existing_commission is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Commission with ID {commission_id} not found",
            )

        # Convert the updated_commission object to a dictionary
        update_dict = updated_commission.dict(exclude_unset=True)

        # Remove the _id field if present, as we don't want to update it
        if "_id" in update_dict:
            del update_dict["_id"]

        # Perform the update operation
        result = collection.update_one(
            {"_id": commission_object_id},
            {"$set": update_dict},
        )

        # Check if any documents were modified
        if result.modified_count > 0:
            return {"message": "Commission updated successfully"}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Commission with ID {commission_id} not found",
            )

    except Exception as e:
        # Log the error for debugging purposes
        print(f"An error occurred: {e}")

        # Raise an HTTPException with a 500 status code
        raise HTTPException(status_code=500, detail="Internal Server Error")


@commission_router.delete(
    "/commissions/{commission_id}", response_description="Delete commission by ID"
)
async def delete_commission(
    commission_id: str,
    # current_user: User = Depends(get_current_user)
):
    # if not (is_admin(current_user)):
    #     raise HTTPException(status_code=403, detail="Unauthorized")
    try:
        print("Deleting commission with ID:", commission_id)
        result = collection.delete_one({"_id": ObjectId(commission_id)})
        if result.deleted_count > 0:
            return {"message": "Commission deleted successfully"}
        else:
            raise HTTPException(
                status_code=404, detail=f"Commission with ID {commission_id} not found"
            )
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
