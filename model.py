from pydantic import BaseModel, ConfigDict, EmailStr, Field
from beanie import Document
import uuid
from typing import Optional


class Commission(BaseModel):
    _id: str
    mongodb_id: str = Field(alias="_id")
    title: str
    description: str
    status: str
    width: str
    color: str
    date: str


    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example":{
                "_id": "1232sdg261foaq3627sf35s",
                "mondodb_id": "1232sdg261foaq3627sf35svfffff",
                "title": "New Drawing",
                "description": "This is a new drawing.",
                "status": "Lineart Completed",
                "width": "50",
                "color": "teal",
                "date":"2024-24-04"
            }
        }

class CommissionRequest(BaseModel):
    title: str
    description: str
    status: str
    width: str
    color: str
    date: str

class Portfolio(BaseModel):
    _id: str
    mongodb_id: str = Field(alias = "_id")
    name: str
    creator: str
    image: str
    description: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example":{
                "_id": "1232sdg261foaq3627sf35s",
                "name": "Eternal Struggle of the Self",
                "creator": "mr. crime",
                #dont bother scrolling
                "image": "data:image/jpeg;base64,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",
                "description":"2024-24-04"
            }
        }


class PortfolioRequest(BaseModel):
    name: str
    creator: str
    image: str
    description:str


class Payment(BaseModel):
    _id: str
    mongodb_id: str = Field(alias = "_id")
    clientId: str
    artistId: str
    status: str
    amount: float

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example":{
                "_id": "1232sdg261foaq3627sf35s",
                "clientId": "2242531s3",
                "artistId": "df8262f42",
                "status": "paid",
                "amount":"10.45"
            }
        }

class PaymentRequest(BaseModel):
    clientId: str
    artistId: str
    status: str
    amount: float


class User(Document):
    email: EmailStr = ""
    password: str = ""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {"email": "python-web-dev@cs.uiowa.edu", "password": "strong!!!"}
        }
    )

    class Settings:
        name = "users"

