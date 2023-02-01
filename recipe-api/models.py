
from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional

class PyObjectId(ObjectId):
    
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invali Objets")
        return ObjectId(v)
    

    @classmethod
    def __modify_schema__(cls, field_name):
        field_name.update(type="String")

class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        json_encoders = {ObjectId: str}

class Menu(MongoBaseModel):
    name: str = Field(..., min_length=3)
    description: str = Field(..., min_length=3)
    cost: float = Field(...)