from pydantic import BaseModel, Field


class Commission(BaseModel):
    _id: str
    mongodb_id: str = Field(alias="_id")
    title: str
    description: str
    status: str
    width: str
    color: str
    date: str


class CommissionRequest(BaseModel):
    title: str
    description: str
    status: str
    width: str
    color: str
    date: str


class User(BaseModel):
    username: str
    password: str


class Portfolio(BaseModel):
    _id: str
    mongodb_id: str = Field(alias="_id")
    name: str
    image: str
    description: str


class PortfolioRequest(BaseModel):
    name: str
    #  image: str
    description: str


class Payment(BaseModel):
    _id: str
    mongodb_id: str = Field(alias="_id")
    status: str
    amount: str


class PaymentRequest(BaseModel):
    status: str
    amount: str
