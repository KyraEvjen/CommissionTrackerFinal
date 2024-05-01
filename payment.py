import os
from dotenv import load_dotenv
from fastapi import APIRouter, Path, HTTPException, status
from model import Payment, PaymentRequest
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from bson import ObjectId
import logging

payment_router = APIRouter()

logger = logging.getLogger(__name__)


payment_list = []
max_id: int = 0

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["CommissionTracker"]
collection = db["payments"]


if "payments" not in db.list_collection_names():
    db.create_collection("payments")


@payment_router.post("/payments", status_code=status.HTTP_201_CREATED)
async def add_payment(payment: PaymentRequest) -> dict:
    clientPost = AsyncIOMotorClient(mongo_uri)
    dbPost = clientPost["CommissionTracker"]
    collectionPost = dbPost["payments"]

    result = await collectionPost.insert_one(payment.model_dump())
    return {
        "message": "payment added successfully",
        "item_id": str(result.inserted_id),
    }


@payment_router.get("/payments", status_code=status.HTTP_200_OK)
async def get_payments() -> dict:
    try:
        data_list = []
        for item in collection.find({}):
            # Include the "_id" field (converted to a string) in the portfol data
            item["_id"] = str(item["_id"])

            item["mongodb_id"] = item["_id"]
            data_list.append(Payment(**item))
        logger.info(f"viewing {len(data_list)} commissions.")
        return {"payments": data_list}
    except Exception as e:
        return JSONResponse(content={"error": str(e)})


@payment_router.get("/payments/{id}")
async def get_payment_by_id(id: str = Path(..., alias="_id")) -> dict:
    try:
        comm = collection.find_one({})
        results = []
        for doc in comm:
            doc["_id"] = str(doc["_id"])
            results.append(doc)
        logger.info(f"viewing payment #{id}.")

        return results
    except Exception as e:
        print(f"error fetching data: {e}")
        return None


@payment_router.put("/payments/{payment_id}", response_description="Update porty by ID")
async def update_payment(payment_id: str, updated_payment: PaymentRequest):
    try:
        # Convert payment_id to ObjectId
        payment_object_id = ObjectId(payment_id)

        # Ensure that the payment_id exists in the database
        existing_payment = collection.find_one({"_id": payment_object_id})
        if existing_payment is None:
            raise HTTPException(
                status_code=404, detail=f"payment with ID {payment_id} not found"
            )

        # Convert the updated_payment object to a dictionary
        update_dict = updated_payment.dict(exclude_unset=True)

        # Remove the _id field if present, as we don't want to update it
        if "_id" in update_dict:
            del update_dict["_id"]

        # Perform the update operation
        result = collection.update_one(
            {"_id": payment_object_id},
            {"$set": update_dict},
        )

        # Check if any documents were modified
        if result.modified_count > 0:
            logger.info(f"Updating payment #{payment_id}.")
            return {"message": "payment updated successfully"}
        else:
            raise HTTPException(
                status_code=404, detail=f"payment with ID {payment_id} not found"
            )

    except Exception as e:
        # Log the error for debugging purposes
        print(f"An error occurred: {e}")

        # Raise an HTTPException with a 500 status code
        raise HTTPException(status_code=500, detail="Internal Server Error")


@payment_router.delete(
    "/payments/{payment_id}", response_description="Delete payment by ID"
)
async def delete_payment(payment_id: str):
    try:
        print("Deleting payment with ID:", payment_id)
        result = collection.delete_one({"_id": ObjectId(payment_id)})
        if result.deleted_count > 0:
            logger.info(f"Deleting payment #{payment_id}")
            return {"message": "payment deleted successfully"}
        else:
            raise HTTPException(
                status_code=404, detail=f"payment with ID {payment_id} not found"
            )
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
