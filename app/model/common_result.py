from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class Result(BaseModel):
    resultCode: int
    resultMessage: str
    resultDescription: str

class Api(BaseModel, Generic[T]):
    result : Result
    body: Optional[T]

