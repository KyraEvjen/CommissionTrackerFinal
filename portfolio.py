import os
from dotenv import load_dotenv
from fastapi import APIRouter, Path, HTTPException, status
from model import Portfolio, PortfolioRequest
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from bson import ObjectId

portfolio_router = APIRouter()

portfolio_list = []
max_id: int = 0


load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["CommissionTracker"]
collection = db["portfolios"]


if "portfolios" not in db.list_collection_names():
    db.create_collection("portfolios")


@portfolio_router.post("/portfolios", status_code=status.HTTP_201_CREATED)
async def add_portfolio(portfolio: PortfolioRequest) -> dict:
    # Connect to MongoDB (use your actual connection details)
    clientPost = AsyncIOMotorClient(mongo_uri)
    dbPost = clientPost["CommissionTracker"]
    collectionPost = dbPost["portfolios"]

    # Insert the porty into MongoDB
    result = await collectionPost.insert_one(portfolio.model_dump())
    print("object id: ", result.inserted_id)
    return {
        "message": "Portfolio added successfully",
        "item_id": str(result.inserted_id),
    }


@portfolio_router.get("/portfolios", status_code=status.HTTP_200_OK)
async def get_portfolios() -> dict:
    try:
        data_list = []
        for item in collection.find({}):
            # Include the "_id" field (converted to a string) in the portfol data
            item["_id"] = str(item["_id"])

            item["mongodb_id"] = item["_id"]
            data_list.append(Portfolio(**item))
        return {"portfolios": data_list}
    except Exception as e:
        return JSONResponse(content={"error": str(e)})


@portfolio_router.get("/portfolios/{id}")
async def get_portfolio_by_id(id: str = Path(..., alias="_id")) -> dict:
    try:
        comm = collection.find_one({})
        results = []
        for doc in comm:
            doc["_id"] = str(doc["_id"])
            print("doc id: ", doc["_id"])
            results.append(doc)
        return results
    except Exception as e:
        print(f"error fetching data: {e}")
        return None


@portfolio_router.put(
    "/portfolios/{portfolio_id}", response_description="Update porty by ID"
)
async def update_portfolio(portfolio_id: str, updated_portfolio: PortfolioRequest):
    try:
        # Convert portfolio_id to ObjectId
        portfolio_object_id = ObjectId(portfolio_id)

        # Ensure that the portfolio_id exists in the database
        existing_portfolio = collection.find_one({"_id": portfolio_object_id})
        if existing_portfolio is None:
            raise HTTPException(
                status_code=404, detail=f"Portfolio with ID {portfolio_id} not found"
            )

        # Convert the updated_portfolio object to a dictionary
        update_dict = updated_portfolio.dict(exclude_unset=True)

        # Remove the _id field if present, as we don't want to update it
        if "_id" in update_dict:
            del update_dict["_id"]

        # Perform the update operation
        result = collection.update_one(
            {"_id": portfolio_object_id},
            {"$set": update_dict},
        )

        # Check if any documents were modified
        if result.modified_count > 0:
            return {"message": "portfolio updated successfully"}
        else:
            raise HTTPException(
                status_code=404, detail=f"Portfolio with ID {portfolio_id} not found"
            )

    except Exception as e:
        # Log the error for debugging purposes
        print(f"An error occurred: {e}")

        # Raise an HTTPException with a 500 status code
        raise HTTPException(status_code=500, detail="Internal Server Error")


@portfolio_router.delete(
    "/portfolios/{portfolio_id}", response_description="Delete portfolio by ID"
)
async def delete_portfolio(portfolio_id: str):
    try:
        print("Deleting portfolio with ID:", portfolio_id)
        result = collection.delete_one({"_id": ObjectId(portfolio_id)})
        if result.deleted_count > 0:
            return {"message": "Portfolio deleted successfully"}
        else:
            raise HTTPException(
                status_code=404, detail=f"Portfolio with ID {portfolio_id} not found"
            )
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
