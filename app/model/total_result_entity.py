
from pydantic import BaseModel


class TatalResult(BaseModel):
    keyword: str
    userInput: str
    dist: str
    ranking: str
