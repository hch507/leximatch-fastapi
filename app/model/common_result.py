from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class ApiError(BaseModel):
    code: str
    message: str

class Payload(BaseModel, Generic[T]):
    data: Optional[T] = None
    error: Optional[ApiError] = None

class CommonResult(BaseModel, Generic[T]):
    resultCode: str
    resultMsg: str
    payload: Payload[T]