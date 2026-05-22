
from pydantic import BaseModel, Field

class HintRequest(BaseModel):
    answer: str
    min_rank: int = Field(alias="minRank")
    max_rank: int = Field(alias="maxRank")
